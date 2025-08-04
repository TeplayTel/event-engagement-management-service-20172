"""
Kafka producer setup and event publisher.
Implements Kafka producer abstraction for event lifecycle topic, using config and logger modules.

SonarQube-compliant: full docstrings, trace logging, error handling, snake_case output fields.
"""
import json
from typing import Any, Dict

from src.config.app_config import Config
from src.logging.logger import get_logger

try:
    from kafka import KafkaProducer
    _KAFKA_AVAILABLE = True
except ImportError:
    _KAFKA_AVAILABLE = False

def to_snake_case_keys(data: dict) -> dict:
    """
    Helper function to transform dictionary keys in data to snake_case recursively.
    ONLY for top-level dicts, messages should be composed properly.
    """
    import re
    def camel_to_snake(s):
        return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

    if not isinstance(data, dict):
        return data
    return {camel_to_snake(key): to_snake_case_keys(value) if isinstance(value, dict) else value for key, value in data.items()}

# PUBLIC_INTERFACE
class EventKafkaPublisher:
    """
    Publishes event lifecycle updates to Kafka,
    using topic/configuration from app config.
    All fields in message will be transformed to snake_case at publish time.
    Usage: publisher = EventKafkaPublisher(); publisher.publish_event(event_dict)
    """
    def __init__(self, kafka_config: Config = None):
        """
        Initializes the Kafka producer using the provided config, or the default App Config.
        Args:
            kafka_config (Config, optional): App config with Kafka connection params.
        """
        self.logger = get_logger(self.__class__.__name__)
        cfg = kafka_config or Config
        self.bootstrap_servers = getattr(cfg, "KAFKA_BOOTSTRAP_SERVERS", None)
        self.event_topic = getattr(cfg, "KAFKA_EVENT_TOPIC", "event_lifecycle")

        if not _KAFKA_AVAILABLE:
            self.logger.error("kafka-python library is not installed. Install with 'pip install kafka-python'.")
            self.producer = None
        else:
            try:
                self.producer = KafkaProducer(
                    bootstrap_servers=self.bootstrap_servers,
                    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                    api_version=(2, 0, 0), # Pin api version for compatibility
                )
                self.logger.info(f"KafkaProducer initialized for {self.bootstrap_servers}; topic={self.event_topic}")
            except Exception as exc:
                self.logger.error(f"Failed to initialize KafkaProducer: {exc}")
                self.producer = None

    # PUBLIC_INTERFACE
    def publish_event(self, message: Dict[str, Any], topic: str = None) -> bool:
        """
        Publishes event lifecycle update to Kafka. Message keys will be snake_case.
        Args:
            message: dict of message fields (will be converted to snake_case recursively).
            topic: Optionally override the configured topic name.
        Returns:
            True if sent successfully, False otherwise.
        """
        if not self.producer:
            self.logger.error("Kafka producer is not initialized; event not published.")
            return False
        
        msg_snake = to_snake_case_keys(message)
        use_topic = topic or self.event_topic
        try:
            self.logger.debug(f"Publishing event to kafka topic={use_topic} payload={msg_snake}")
            fut = self.producer.send(use_topic, value=msg_snake)
            result = fut.get(timeout=10)
            self.logger.info(f"Event published to {use_topic}, partition={result.partition}, offset={result.offset}")
            return True
        except Exception as exc:
            self.logger.error(f"Kafka publish failed: {exc} | topic={use_topic}")
            return False

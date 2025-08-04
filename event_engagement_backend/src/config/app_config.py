"""
App config loader and environment setup.
"""
import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env

# PUBLIC_INTERFACE
class Config:
    """
    Application configuration, loaded from environment variables.
    """
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGODB_DB = os.getenv("MONGODB_DB")
    KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
    KAFKA_EVENT_TOPIC = os.getenv("KAFKA_EVENT_TOPIC", "event_lifecycle")
    # Add other config keys as needed with clear env-driven approach

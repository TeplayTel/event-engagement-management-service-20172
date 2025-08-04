"""
Logging utility setup following SonarQube/code quality requirements.
"""

import logging
import sys

# PUBLIC_INTERFACE
def get_logger(name: str = "event_engagement_backend"):
    """
    Returns a logger with structured debug/info/error support.
    """
    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s %(name)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger

# Debug logger example for reference (for developer use):
logger = get_logger()
logger.debug("Debug logger initialized (template debug message).")

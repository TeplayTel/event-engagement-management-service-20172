"""
Data source domain model(s).
"""

from enum import Enum
from typing import Optional


# PUBLIC_INTERFACE
class DataSourceType(Enum):
    """Enum for available data source types."""
    API = "api"
    FILE = "file"
    MANUAL = "manual"


# PUBLIC_INTERFACE
class DataSourceConfig:
    """
    Domain model for data source configuration.
    Attributes use camelCase for POJO use.
    """

    def __init__(
        self,
        configId: str,
        type: str,
        endpoint: Optional[str] = None,
        authToken: Optional[str] = None,
        details: Optional[dict] = None,
    ):
        self.configId = configId
        self.type = type
        self.endpoint = endpoint
        self.authToken = authToken
        self.details = details

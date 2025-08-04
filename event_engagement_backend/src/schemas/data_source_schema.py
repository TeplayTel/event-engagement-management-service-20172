"""
Pydantic schemas for data source config.
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict

# PUBLIC_INTERFACE
class DataSourceConfigRequest(BaseModel):
    """
    Schema for data source creation request.
    """
    type: str = Field(..., description="Data source type (api, file, manual)")
    endpoint: Optional[str] = Field(None, description="API endpoint or file path")
    auth_token: Optional[str] = Field(None, description="Authentication token, if applicable")
    details: Optional[Dict] = Field(None, description="Extra settings/config for the source")


# PUBLIC_INTERFACE
class DataSourceConfigResponse(BaseModel):
    """
    Schema for returned data source configuration.
    """
    id: str = Field(..., description="Config ID")
    type: str = Field(..., description="Data source type")
    endpoint: Optional[str] = Field(None, description="API endpoint or file path")
    details: Optional[Dict] = Field(None, description="Extra settings/config for the source")
    # Add created_at, updated_at if required

"""
Pydantic schemas for data source config.
"""

from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class DataSourceConfigRequest(BaseModel):
    """Schema for data source creation request."""
    type: str = Field(..., description="Data source type")
    # Additional fields

# PUBLIC_INTERFACE
class DataSourceConfigResponse(BaseModel):
    """Schema for returned data source configuration."""
    id: str = Field(..., description="Config ID")
    type: str = Field(..., description="Data source type")
    # Additional fields

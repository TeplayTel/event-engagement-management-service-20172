"""
Pydantic schemas for event requests and responses.
"""

from pydantic import BaseModel, Field

# PUBLIC_INTERFACE
class EventCreateRequest(BaseModel):
    """Schema for creating an event (API request body)."""
    name: str = Field(..., description="Event name")
    # Add more fields according to requirements

# PUBLIC_INTERFACE
class EventResponse(BaseModel):
    """Schema for returning event details in API responses."""
    id: str = Field(..., description="Event ID")
    name: str = Field(..., description="Event name")
    # Add more fields according to requirements

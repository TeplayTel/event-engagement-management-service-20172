"""
Timeline log domain model(s).
"""

from enum import Enum
from typing import Optional
from datetime import datetime


# PUBLIC_INTERFACE
class TimelineAction(Enum):
    STARTED = "started"
    UPDATED = "updated"
    COMPLETED = "completed"
    ABORTED = "aborted"


# PUBLIC_INTERFACE
class TimelineStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


# PUBLIC_INTERFACE
class EventTimeline:
    """
    Domain model representing an event's timeline entry.
    Attributes follow camelCase convention.
    """

    def __init__(
        self,
        recordId: str,
        eventId: str,
        action: str,
        timestamp: datetime,
        status: str = TimelineStatus.PENDING.value,
        details: Optional[dict] = None,
        logs: Optional[str] = None,
    ):
        self.recordId = recordId
        self.eventId = eventId
        self.action = action
        self.timestamp = timestamp
        self.status = status
        self.details = details
        self.logs = logs

"""
App-wide constants, enums, and field names for consistency.
"""

# Paging
DEFAULT_PAGE_SIZE = 20

# Collection names for MongoDB
COLLECTION_EVENTS = "event_metadata"
COLLECTION_DATA_SOURCES = "event_data_source"
COLLECTION_TIMELINES = "event_timelines"

# Kafka topic(s)
EVENT_LIFECYCLE_TOPIC = "event_lifecycle"

# Status values for event and timelines
EVENT_STATUS_CREATED = "created"
EVENT_STATUS_IN_PROGRESS = "in_progress"
EVENT_STATUS_COMPLETED = "completed"
EVENT_STATUS_FAILED = "failed"

TIMELINE_ACTION_STARTED = "started"
TIMELINE_ACTION_UPDATED = "updated"
TIMELINE_ACTION_COMPLETED = "completed"
TIMELINE_ACTION_ABORTED = "aborted"

# Data Source types
DATA_SOURCE_TYPE_API = "api"
DATA_SOURCE_TYPE_FILE = "file"
DATA_SOURCE_TYPE_MANUAL = "manual"

# Utility constant
DATETIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"

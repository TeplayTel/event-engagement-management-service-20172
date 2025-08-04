"""
MongoDB interaction logic for data source configs.
"""

# PUBLIC_INTERFACE
class DataSourceRepository:
    """
    Handles DB persistence for data source configs.
    """
    def __init__(self, db):
        self.db = db

    # PUBLIC_INTERFACE
    def insert_config(self, config_data: dict):
        """Insert config record (snake_case)."""
        pass

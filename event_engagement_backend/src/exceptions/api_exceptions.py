"""
API and business logic exception definitions.
"""

class AppException(Exception):
    """Base application exception."""

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

# PUBLIC_INTERFACE
class NotFoundException(AppException):
    """Exception raised when entity is not found."""
    pass

# PUBLIC_INTERFACE
class ValidationException(AppException):
    """Exception raised for validation errors."""
    pass

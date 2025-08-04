"""
Helpers for API response formatting and output consistency.
"""

# PUBLIC_INTERFACE
def api_success(data, message: str = "Success"):
    """Package success response."""
    return {"status": "success", "data": data, "message": message}

# PUBLIC_INTERFACE
def api_error(message: str, code: int = 400):
    """Package error response."""
    return {"status": "error", "message": message, "code": code}

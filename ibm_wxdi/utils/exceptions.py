class WXDIError(Exception):
    """Base exception for the SDK."""


class AuthenticationError(WXDIError):
    """Raised when authentication fails."""

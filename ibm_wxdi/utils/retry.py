import time
from functools import wraps


def retry(times: int = 3, delay: float = 1.0):
    """Simple retry decorator."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
                    time.sleep(delay)

        return wrapper

    return decorator

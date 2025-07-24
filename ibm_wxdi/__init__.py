"""ibm-wxdi SDK."""

from importlib import metadata

try:
    __version__ = metadata.version("ibm-wxdi")
except metadata.PackageNotFoundError:  # pragma: no cover - package not installed
    __version__ = "0.0.0"

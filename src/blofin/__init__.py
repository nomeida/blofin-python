from importlib.metadata import version, PackageNotFoundError
from .client import BloFinClient  # Import the BloFinClient class

try:
    __version__ = version("blofin")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

# Expose BloFinClient at the package level
__all__ = ['BloFinClient']
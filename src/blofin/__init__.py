from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("blofin")
except PackageNotFoundError:
    # package is not installed
    __version__ = "unknown"

# Rest of your __init__.py content
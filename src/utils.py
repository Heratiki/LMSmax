import logging
from typing import Any

def setup_logger(name: str) -> logging.Logger:
    """Set up a logger with a specific name."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    return logger

def validate_config(config: Any) -> bool:
    """Validate configuration data."""
    # Placeholder for validation logic
    return True
import pytest # type: ignore
import logging
from src.utils import setup_logger, validate_config

def test_setup_logger():
    """Test logger setup function."""
    logger = setup_logger("test_logger")
    assert isinstance(logger, logging.Logger)
    assert logger.name == "test_logger"
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == 1
    assert isinstance(logger.handlers[0], logging.StreamHandler)

def test_validate_config():
    """Test configuration validation."""
    test_config = {
        "LM_STUDIO_API_URL": "http://localhost:1234",
        "LM_STUDIO_API_KEY": "test_key"
    }
    assert validate_config(test_config) == True
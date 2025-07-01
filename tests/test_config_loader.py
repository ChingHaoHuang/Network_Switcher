import pytest
from main import load_config

def test_load_config_returns_dict():
    """
    Tests that the load_config() function reads the config.ini file
    and returns a dictionary.
    """
    config = load_config()
    assert isinstance(config, dict)

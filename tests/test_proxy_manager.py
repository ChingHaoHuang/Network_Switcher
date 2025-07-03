import pytest
from src.proxy_manager import set_proxy

@pytest.mark.integration
def test_set_proxy_successfully():
    """
    Tests that set_proxy() can successfully configure the system proxy.
    This is a functional/integration test and requires careful handling.
    """
    proxy_server = "http://127.0.0.1:8888"  # A dummy proxy server
    
    # The function should return True on success
    assert set_proxy(proxy_server) is True

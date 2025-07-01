import pytest
from main import set_proxy

@pytest.mark.skip(reason="This test requires administrative privileges and interacts with the live system's proxy settings.")
def test_set_proxy_successfully():
    """
    Tests that set_proxy() can successfully configure the system proxy.
    This is a functional/integration test and requires careful handling.
    """
    proxy_server = "http://127.0.0.1:8888"  # A dummy proxy server
    
    # The function should return True on success
    assert set_proxy(proxy_server) is True

import pytest
from main import add_route

@pytest.mark.skip(reason="This test requires administrative privileges and interacts with the live system's routing table.")
def test_add_route_successfully():
    """
    Tests that add_route() can successfully add a new network route.
    This is more of a functional/integration test and requires careful handling.
    """
    target_host = "1.2.3.4"  # A dummy target
    gateway = "192.168.1.1" # A common gateway
    
    # The function should return True on success
    assert add_route(target_host, gateway) is True

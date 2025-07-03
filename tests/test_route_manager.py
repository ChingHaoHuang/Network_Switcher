import pytest
from src.route_manager import add_route, delete_route

@pytest.mark.integration
def test_add_and_delete_route_successfully():
    """
    Tests that add_route() can successfully add and then delete a new network route.
    This is more of a functional/integration test and requires careful handling.
    """
    target_host = "8.8.8.8"  # A public DNS server, less likely to conflict
    gateway = "192.168.1.1" # A common gateway, might need adjustment
    
    # Add the route and assert success
    assert add_route(target_host, gateway) is True
    
    # Delete the route and assert success
    assert delete_route(target_host) is True

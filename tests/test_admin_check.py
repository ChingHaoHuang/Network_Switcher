import pytest
from src.admin_checker import is_admin

def test_is_admin_returns_boolean():
    """
    Tests that the is_admin() function returns a boolean value.
    This test will fail initially because the function doesn't exist.
    """
    # This test doesn't need to check for True or False, just that
    # the function runs and returns a boolean. The actual check
    # for admin rights is hard to test in a unit test, so we
    # trust the implementation and just check its interface.
    result = is_admin()
    assert isinstance(result, bool)

import pytest
import os
from main import sync_hosts_file

# A known-good, simple hosts file content for testing
TEST_HOSTS_CONTENT = """
127.0.0.1 localhost
::1 localhost
"""

@pytest.fixture
def temp_hosts_file(tmp_path):
    """Create a temporary source hosts file for testing."""
    source_file = tmp_path / "test_hosts"
    source_file.write_text(TEST_HOSTS_CONTENT, encoding="utf-8")
    return str(source_file)

@pytest.fixture
def temp_system_hosts_file(tmp_path):
    """Create a temporary, fake system hosts file for testing."""
    dest_file = tmp_path / "system_hosts"
    # Start with different content to ensure it gets overwritten
    dest_file.write_text("1.1.1.1 old-entry", encoding="utf-8")
    return str(dest_file)

def test_sync_hosts_file_successfully(temp_hosts_file, temp_system_hosts_file):
    """
    Tests that sync_hosts_file can correctly copy content from a source
    to a destination hosts file.
    """
    # The function should return True on success
    assert sync_hosts_file(temp_hosts_file, temp_system_hosts_file) is True
    
    # Verify the content was copied correctly
    with open(temp_system_hosts_file, 'r', encoding='utf-8') as f:
        content = f.read()
    assert content == TEST_HOSTS_CONTENT

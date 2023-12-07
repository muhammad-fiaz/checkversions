import pytest
from checkversions.checkversions import compare_versions

@pytest.fixture(params=[
    ("2.0.0-release", "v2.0.1", "v2.0.1"),  # Current version is older
    ("v1.0.0", "1.0.0-beta", "v1.0.0"),  # Current version is newer
    ("v3.1.2", "v3.1.2", "v3.1.2"),  # Versions are the same
    ("v2.0.0-beta", "2.0.1", "v2.0.1"),  # Current version is older with hyphen
    ("v1.0.0", "v1.0.0-beta", "v1.0.0"),  # Current version is newer with hyphen
    ("v3.1.2", "v3.1.2", "v3.1.2"),  # Versions are the same with hyphen
    ("v2.0.0-beta", "v2.0.1-alpha", "v2.0.1-alpha"),  # Current version is older with hyphen and words
    ("v1.0.0-beta", "1.0.0-alpha", "v1.0.0-alpha"),  # Current version is newer with hyphen and words
    ("v3.1.2-beta", "v3.1.2-alpha", "v3.1.2-alpha"),  # Versions are the same with hyphen and words
    ("v2.0.0-beta", "v2.0.1", "v2.0.1"),  # Current version is older with words
    ("v1.0.0-beta", "1.0.0", "v1.0.0"),  # Current version is newer with words
])
def version_data(request):
    """
    Fixture providing version data for testing.

    Each parameter is a tuple containing three elements:
    1. Current version
    2. Latest version
    3. Expected result of the version comparison

    Returns:
        tuple: A set of version data for testing.
    """
    return request.param

def test_compare_versions(version_data):
    """
    Test the compare_versions function with different version scenarios.

    Args:
        version_data (tuple): A tuple containing current_version, latest_version, and expected_result.

    The test compares two versions using the compare_versions function and asserts that the result
    matches the expected outcome.
    """
    current_version, latest_version, expected_result = version_data
    result = compare_versions(current_version, latest_version)
    assert result == expected_result

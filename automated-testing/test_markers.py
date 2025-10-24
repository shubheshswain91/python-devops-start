import pytest

try:
    import some_optional_library  # type: ignore[import]
except:
    some_optional_library = None

# Section: Skipping Tests Unconditionally: @pytest.mark.skip
@pytest.mark.skip("This test is temporarily disabled")
def test_new_experimental_feature():
    assert False, "This test should be skipped"

# Section: Skipping Tests Conditionally: @pytest.mark.skipif
@pytest.mark.skipif(
        some_optional_library is None, 
        reason="Optional dependency not installed"
    )
def test_with_optional_dependency() -> None:
    print(f"Running test with optional library: {some_optional_library}")
    assert some_optional_library


# Section: Expected Failures: @pytest.mark.xfail

# Section: Custom Markers and Registration

# Section: Running Tests by Marker (m option)

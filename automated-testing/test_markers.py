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

@pytest.mark.xfail(reason="Bug #123: Division by zero not handled properly.")
def test_division_by_zero() -> None:
    _division = 1 / 0  # This will raise a ZeroDivisionError
    assert False

@pytest.mark.xfail    # Add strict=True to make XPASS lead to a failure
def test_expected_to_fail() -> None:    
    assert True

# Section: Custom Markers and Registration

# Section: Running Tests by Marker (m option)

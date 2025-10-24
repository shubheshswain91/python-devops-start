# Section: The `assert` Statement

# Uncoment the following lines to see the assertion failure
# x: int = 5
# assert x == 5
# assert x == 6, 'x should be 5'

# Section: Pytest and `assert`

def test_string_equality() -> None:
    expected_status = "SUCCESS"
    actual_status = "success".upper()

    assert expected_status == actual_status, f'Expected "{expected_status}" but got "{actual_status}"'
# Section: Pytest’s Rich Failure Output

# Section: Asserting Floating-Point Numbers (`pytest.approx`)

# Section: Asserting Exceptions (`pytest.raises`)


# commands to run the tests
# pytest 

# pytest -v # to see the verbose output

# pytest -r # to show failed tests

# pytest -ra # to show all tests, including skipped ones

# pytest -rA # to show all tests, including skipped ones, and show their source code 
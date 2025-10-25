import pytest


def is_valid_hostname_char(char: str) -> bool:
    if "a" <= char <= "z":
        return True
    if "0" <= char <= "9":
        return True
    if char == "-":
        return True
    return False


def check_url_status(url: str) -> tuple[int | str, str]:
    if url == "https://google.com":
        return (200, "OK")
    if url == "https://fakesite123.org/notfound":
        return (404, "HTTP_ERROR (404)")
    if url == "http://httpbin.org/status/503":
        return (503, "HTTP_ERROR (503)")
    if url == "http://localhost:1":
        return ("CONNECTION_ERROR", "CONNECTION_ERROR")
    return ("UNKNOWN", "UNKNOWN")


# Section: The Problem: Duplicated Test Logic

""" 
a -> True
5 -> True
- -> True
A -> False
_ -> False
 """

def test_is_valid_lowercase_char() -> None:
    assert is_valid_hostname_char("a") is True

def test_is_valid_5() -> None:    
    assert is_valid_hostname_char("5") is True

def  test_is_valid_hyphen() -> None:    
    assert is_valid_hostname_char("-") is True

def test_is_valid_uppercase_char() -> None:    
    assert is_valid_hostname_char("A") is False    

def test_is_valid_underscore() -> None:    
    assert is_valid_hostname_char("_") is False    

# Section: Solution: @pytest.mark.parametrize

@pytest.mark.parametrize(
    "input_char, expected_result",
    [
        ("a", True),
        ("5", True), 
        ("-", True), 
        ("A", False), 
        ("_", False)  # more test cases...  # (Note: You can add as many test cases as you want)
    ]
)

def test_is_valid_hostname_char(
    input_char: str,
    expected_result: bool,
):
    assert is_valid_hostname_char(input_char) is expected_result

# Section: Customizing Test IDs with pytest.param construct

@pytest.mark.parametrize(
    "url_to_check, expected_status_code, expected_status_text",
    [
    ("https://google.com", 200, "OK"),
    ("https://fakesite123.org/notfound", 404, "HTTP_ERROR (404)"),
    ("http://httpbin.org/status/503", 503, "HTTP_ERROR (503)"),
    ("http://localhost:1", "CONNECTION_ERROR", "CONNECTION_ERROR"),
    pytest.param(
        "https://pending.retries.tests", 503,"HTTP_ERROR (503)", marks=pytest.mark.xfail(reason="retry logic for 503 is not yet implemented"))  # (Note: You can add more test
    ],
    ids=[
        "google_ok",
        "site_not_found",
        "server_error_503",
        "connection_error",
        "xfail_retry_case"
    ]    
)

def test_various_urls_statuses(
    url_to_check: str, expected_status_code: int, expected_status_text: str
):
    status_code, status_text = check_url_status(url_to_check)
    assert status_code == expected_status_code
    assert status_text == expected_status_text

    
    
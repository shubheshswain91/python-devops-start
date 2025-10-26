import subprocess
from unittest.mock import MagicMock
from pytest_mock import MockerFixture
from dummy_functions import get_current_user, check_file_exists, fetch_both_endpoints

# Section: Using side_effect - Exceptions

def test_get_current_user_command_fails(mocker: MockerFixture):
    mock_run = mocker.patch("dummy_functions.subprocess.run")
    mock_run.side_effect = subprocess.CalledProcessError(
        returncode=1,
        cmd=["whoami"]
    )

    result = get_current_user()

    assert result is None

# Section: Using side_effect - List for Multiple Calls

def test_check_file_exists_side_effects_list(mocker: MockerFixture):
    mock_exists = mocker.patch("dummy_functions.os.path.exists")
    mock_exists.side_effect = [True, False]

    assert check_file_exists("file1.txt") is True
    assert check_file_exists("file2.txt") is False

    assert mock_exists.call_count == 2

    

    assert [call.args[0] for call in mock_exists.call_args_list] == [("file1.txt"), ("file2.txt")]

# Section: Using side_effect - Callable for Multiple Calls

def test_fecth_both_endpoints_by_url(mocker: MockerFixture):
    fake_responses: dict[str, MagicMock] = {}

    for url, data in [
        ("https://api.example.com/first", {"first": "data"}),
        ("https://api.example.com/second", {"second": "data"}),
    ]:
        resp = mocker.MagicMock()
        resp.status_code = 200
        resp.json.return_value = data

        fake_responses[url] = resp

    def _fake_get(url: str) -> MagicMock:
        return fake_responses[url]
    
    mocker.patch("dummy_functions.requests.get", side_effect=_fake_get)

    result = fetch_both_endpoints()

    assert result == ({"first": "data"}, {"second": "data"})


# Section: Choosing between Mock and MagicMock

from unittest.mock import patch, Mock, MagicMock
from dummy_functions import check_file_exists 
from pytest_mock import MockerFixture

# Section: Using unittest.mock.patch

def test_check_file_exists_manual_patch() -> None:
    filepath = "/path/to/some/file.txt"

    patcher = patch("dummy_functions.os.path.exists")

    mock_exists = patcher.start()

    mock_exists.return_value = True

    try:
        result = check_file_exists(filepath=filepath)
        mock_exists.assert_called_once_with(filepath)
        assert result is True
    finally:
        patcher.stop()    


def test_check_file_exists_context_manager() -> None:
    filepath = "/path/to/some/file.txt"

    with patch("dummy_functions.os.path.exists") as mock_exists:
        mock_exists.return_value = True
        result = check_file_exists(filepath=filepath)
        mock_exists.assert_called_once_with(filepath)
        assert result is True

@patch("dummy_functions.os.path.exists")
def test_check_file_exists_decorator(mock_exists: Mock) -> None:
    filepath = "/path/to/some/file.txt"
    mock_exists.return_value = True
    result = check_file_exists(filepath=filepath)
    mock_exists.assert_called_once_with(filepath)
    assert result is True        
    

def test_check_file_pytest_mocker(mocker: MockerFixture) -> None:
    filepath = "/path/to/some/file.txt"

    mock_exists = mocker.patch("dummy_functions.os.path.exists")

    mock_exists.return_value = True
    result = check_file_exists(filepath=filepath)
    mock_exists.assert_called_once_with(filepath)
    assert result is True    

# Section: MagicMock and Configuring Mock Objects

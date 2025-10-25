import pytest
from pathlib import Path
from typing import Iterator
import tempfile
# Section: Defining a Simple Fixture with @pytest.fixture

ConfigDict = dict[str, str | int]

@pytest.fixture
def sample_config_dict() -> ConfigDict:
    return {
        "api_url": "https://api.example.com",
        "timeout": 10,
        "retries": 3
    }

def test_api_url_is_present(sample_config_dict: ConfigDict):
    print(f" [Test]:  test_api_url is present running...")
    assert "api_url" in sample_config_dict
    assert sample_config_dict["api_url"]  == "https://api.example.com"

@pytest.fixture
def temp_config_file() -> Iterator[Path]:
    temp_file = tempfile.NamedTemporaryFile(
        mode="w+t", encoding="utf-8", suffix=".yaml", delete=False
    )        
    temp_file_path = Path(temp_file.name)
    print(f"\n  [FIXTURE SETUP]:  Temporary config file created at: {temp_file_path}")
    temp_file.write("Setting1: value1\nSetting2: value2\n")
    temp_file.close()
    yield temp_file_path
    print(f"\n  [FIXTURE TEARDOWN]:  temp config file deleting: {temp_file_path}")

    if temp_file_path.exists():
        temp_file_path.unlink()

def test_read_from_temp_file(temp_config_file: Path):
    print(" [Test]:  test_read_from_temp_file running...")
    assert temp_config_file.exists()
    content = temp_config_file.read_text(encoding="utf-8")
    assert "Setting1: value1" in content


# Section: Using Fixtures in Test Functions

# Section: Fixture Scope and Lifecycle

# Section: Sharing Fixtures with conftest.py

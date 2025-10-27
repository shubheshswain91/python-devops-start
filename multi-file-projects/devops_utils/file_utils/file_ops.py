print("Module file ops is being imported")

from typing import Any
try:
    import yaml
except (ModuleNotFoundError, ImportError) as e:    
    print("PyYAML is not installed. YAML parsing functionality will be limited.")
    yaml = None


SUPPORTED_EXTENSIONS: list[str] = [".json", ".yaml", ".txt"]

def check_file_extension(filename: str) -> bool:
    """ Checks if the given filename has a supported extension. """
    print(f"  -- file_ops.check_file_extension called  for {filename}")
    return any(filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS)


def parse_yaml_file(path_str: str) -> dict[str, Any]:
    """ Parses a YAML file and returns its contents as a dictionary. """
    print(f"  -- file_ops.parse_yaml_file called  for {path_str}")
    if yaml:
        with open(path_str, 'r') as file:
            return yaml.safe_load(file)
    else:
        return {}
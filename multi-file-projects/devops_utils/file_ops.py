print("Module file ops is being imported")

SUPPORTED_EXTENSIONS: list[str] = [".json", ".yaml", ".txt"]

def check_file_extension(filename: str) -> bool:
    """ Checks if the given filename has a supported extension. """
    print(f"  -- file_ops.check_file_extension called  for {filename}")
    return any(filename.endswith(ext) for ext in SUPPORTED_EXTENSIONS)
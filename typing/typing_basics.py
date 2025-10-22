# Section: Basic Type Hint Syntax - Variable Annotations

config_path: str = "/path/to/config.ini"
retry_count: int = 3
is_enalbed: bool = bool(1)
servers: list[str] = ["server1", "server2", "server3"]
settings: dict[str, int | str] = {
    "port": 8080,
    "username": "admin"
} 

# Section: Basic Type Hint Syntax - Function Argument and Return Type Annotations
def get_server_status(hostaname: str, port: int) -> str:
    print(f"Checking {hostaname}")
    if port == 80:
        return "Server is up"
    else:
        return "Server is down"

# Section: Python Remains Dynamically Typed

# Demonstration of dynamic typing

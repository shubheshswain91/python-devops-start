from typing import Optional, Any

# Section: Typing Lists

hostnames: list[str]= ['web01.example1.com', 'db01.example2.com', 'example3.com']
open_ports: list[int] = [80, 443, 8080, 22]

def process_hostnames(hostnames: list[str]) -> None:
    for hostname in hostnames:
        print(f"Processing hostname: {hostname.upper()}")

process_hostnames(hostnames)
# process_hostname(open_ports)  # This will raise a TypeError

# Section: Typing Dictionaries

server_config: dict[str, str] = {
    'hostname': 'web01.example1.com',
    'ip_address': '192.168.1.1',
    'os': 'Ubuntu 20.04'
}

user_roles: dict[str, list[str]] = {
    'user1': ['admin', 'developer'],
    'user2': ['developer']
}
# Section: Typing Tuples

server_status: tuple[str, int, bool] = (
    "api.example.com",
    200,
    True
)
ip_parts: tuple[int, ...] = (192, 168, 1, 1)


# Section: Typing Sets
admin_users: set[str] = {"admin", "user1", "user2"}

def is_admin(username: str, admins: str) -> bool:
    return username in admins

# Section: Union[X, Y, ...] for Multiple Possible Types
identifier: str|int = "example_identifier"
identifier = str(123)

def process_mixed_data(data: list[int|str]) -> None:   # It's statics type checking and it will fail if the data contains a mixed type during runtime execution.
    for item in data:
        if isinstance(item, str):
            print(f"Processing string: {item.upper()}")
        else:
            print(f"Processing number: {item * 2}")   
                      

# Section: Optional[X] for Values That Can Be None

def find_user(user_id: str) -> Optional[dict[str, str]]:
    if user_id == "123":
        return {"id": "123", 
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
    return None

found_user = find_user("123")
print(f"User found: {found_user["name"]}")

# Section: Any for Unrestricted Types
def print_anything(item: Any) -> None:
    print(f"Item: {item}, type: {type(item)}")

print_anything("Hello, World!")
print_anything(123)

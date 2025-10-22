from typing import TypedDict, NotRequired

class User(TypedDict):
    id: int
    name: str
    email: str
    phone: NotRequired[str]

user: User = {
    "id": 1,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone": "+12345678"
}    

print(f"User data: {user.get("email")}")
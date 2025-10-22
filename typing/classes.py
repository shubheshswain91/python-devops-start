from typing import Self

# Section: Classes as Type Hints

class Server:
    def __init__(self, hostname: str, ip_address: str, os_type: str = "Linux"):
        self.hostname: str = hostname
        self.ip_address: str = ip_address
        self.os_type: str = os_type
        self.is_online: bool = False

    def connect(self) -> None:
        print(f"Connecting to {self.hostname} ({self.ip_address})")
        self.is_online = True
        print(f" {self.hostname} is online")    

    def get_status(self) -> str:
        return "online" if self.is_online else "offline"  

def deploy_app_to_server(target_server: Server, app_name: str) -> bool:  
    print(f"Deploying {app_name} to {target_server.hostname}")

    if not target_server.is_online:
        target_server.connect()

    print(f"Deployment of {app_name} to {target_server.hostname} successful")
    return True

web_server = Server(hostname="web-server", ip_address="192.168.0.1")        
db_server = Server(hostname="db-server", ip_address="192.168.0.2")

deploy_app_to_server(target_server=web_server, app_name="Django")
deploy_app_to_server(target_server=db_server, app_name="PostgreSQL")

# Section: Hinting Methods Within a Class

class Calculator:
    def __init__(self, initial_value: int | float = 0):
        self.total: int | float = initial_value

    def add(self, value: int | float) -> Self:
        self.total += value
        return self  # Returning the instance for chaining operations

    def subtract(self, value: int | float) -> Self:
        self.total -= value   
        return self  # Returning the instance for chaining operations    

    def multiply(self, value: int | float) -> Self:
        self.total *= value
        return self  # Returning the instance for chaining operations
    
    def divide(self, value: int | float) -> Self:
        self.total /= value
        return self  # Returning the instance for chaining operations

    def get_total(self) -> int | float:
        return self.total        

my_calc = Calculator()

print(my_calc.add(5).subtract(3).multiply(2).get_total())  

# Section: Forward References (Strings)

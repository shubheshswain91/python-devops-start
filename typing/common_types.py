# Section: Typing Lists

hostnames: list[str]= ['web01.example1.com', 'db01.example2.com', 'example3.com']
open_ports: list[int] = [80, 443, 8080, 22]

def process_hostnames(hostnames: list[str]) -> None:
    for hostname in hostnames:
        print(f"Processing hostname: {hostname.upper()}")

process_hostnames(hostnames)
# process_hostname(open_ports)  # This will raise a TypeError
# Section: Typing Dictionaries

# Section: Typing Tuples

# Section: Typing Sets

# Section: Union[X, Y, ...] for Multiple Possible Types

# Section: Optional[X] for Values That Can Be None

# Section: Any for Unrestricted Types

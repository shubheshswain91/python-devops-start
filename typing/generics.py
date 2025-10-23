from typing import Optional, TypeVar

# Section: Defining a generic function to get the first item of a list

T = TypeVar('T')
def get_first_item(
        input_list: list[T]
        ) -> Optional[T]:
    if input_list:
        return input_list[0]


first_number = get_first_item([1, 2, 3])
first_str = get_first_item(['apple', 'banana', 'cherry'])
first_mixed_list = get_first_item([1, 'apple', 3.14])

# Section: Constrained TypeVar for numeric addition
NumberType = TypeVar('NumberType', int, float)

def add_generic_number(x: NumberType, y: NumberType) -> NumberType:
    return x + y

sum_int = add_generic_number(5, 3.0)

# Section: Bounded TypeVar with deployed filter for DevOps resources

class CloudResource:
    def __init__(self, name: str, cpu_usage: float) -> None:
        self.name: str = name
        self.cpu_usage: float = cpu_usage
        self.deployed: bool = False

    def deploy(self) -> None:
        print(f"Deploying {self.name}...")
        self.deployed = True

class VirtialMachine(CloudResource):
    def reboot(self) -> None:
        print(f"Rebooting {self.name}...")

class DockerContainer(CloudResource):
    def restart(self) -> None:
        print(f"Restarting container {self.name}...")                    



ResourceType = TypeVar('ResourceType', bound=CloudResource)
def filter_deployment(resources: list[ResourceType]) -> list[ResourceType]:
    return [resource for resource in resources if resource.deployed]

vm1 = VirtialMachine("VM1", cpu_usage=0.5)
vm2 = VirtialMachine("VM2", cpu_usage=0.8)
container1 = DockerContainer("api-service", cpu_usage=0.7)
container2 = DockerContainer("worker", cpu_usage=0.9)


all_resources = [vm1, vm2, container1, container2]
deployed_resources = filter_deployment(all_resources)

# Section: Generic class SimpleStack

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

# Section: Generic class SimpleStack

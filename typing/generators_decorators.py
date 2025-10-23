# Section: Typing Decorators (simple_logging_decorator)

from typing import Callable, Any, TypeVar, ParamSpec, Generator, Iterable
import functools


def simple_logging_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with arguments {args}, {kwargs}")
        return result
    return wrapper
@simple_logging_decorator
def add(a: int, b: int) -> int:
    return a + b

result_add = add(5, 10)
# Section: Typing Decorators (better_logging_decorator with TypeVar)

P = ParamSpec('P')
R = TypeVar('R')


def better_logging_decorator(func: Callable[P,R]) -> Callable[P,R]:
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> Any:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with arguments {args}, {kwargs}")
        return result
    return wrapper
@better_logging_decorator
def subract(a: int, b: int) -> int:
    return a - b

result_sub = subract(5, 10)

# Section: Typing Generators

def count_up_to(limit: int) -> Generator[int, None, str]:
    for i in range(limit):
        yield i

    return "Counting completed"    

def accumulate_and_send() -> Generator[float, float | None, None]:
    total = 0.0
    try:
        while True:
            sent = yield total
            if sent:
                total += sent
    except GeneratorExit:
        pass 

test_accumulate = accumulate_and_send()    
next(test_accumulate)  # Start the generator        
print(test_accumulate.send(1.0))  # Send an initial value
print(next(test_accumulate) ) # Send another value)
print(test_accumulate.send(2.0))  # Send another value
print(test_accumulate.send(3.0))  # Send another value
print(test_accumulate.send)  

# Section: Iterable & Iterator

def process_items(items: Iterable[str]) -> list[str]:
    return [item.upper() for item in items]

print(process_items(["apple", "banana", "cherry"]))
print(process_items(("apple", "banana", "cherry")))
print(process_items({"apple", "banana", "cherry"}))
print(process_items({"a":"b", "hello": "world"}))

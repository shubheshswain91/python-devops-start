# Section: Typing Decorators (simple_logging_decorator)

from typing import Callable, Any, TypeVar
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
F = TypeVar('F', bound=Callable[..., Any])
def better_logging_decorator(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} called with arguments {args}, {kwargs}")
        return result
    return wrapper # type: ignore [return-value]
@better_logging_decorator
def subract(a: int, b: int) -> int:
    return a - b

result_sub = subract(5, 10)
# Section: Typing Generators

# Section: Iterable & Iterator
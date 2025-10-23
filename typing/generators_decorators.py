# Section: Typing Decorators (simple_logging_decorator)

from typing import Callable, Any, TypeVar, ParamSpec
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



# Section: Iterable & Iterator
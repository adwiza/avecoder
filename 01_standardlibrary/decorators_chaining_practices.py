from inspect import signature


def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    wrapper.__signature__ = signature(func)
    wrapper.__doc__ = func.__doc__
    return wrapper


@decorator_1
def add(x: int, y: int) -> int:
    """Returns the sum of x and y."""
    print(x + y)


# add(5, 2)

def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def decorator_2(func):
    def wrapper(x, y, *args, **kwargs):
        return func(x, y, *args, **kwargs)
    return wrapper


@decorator_1
@decorator_2
def add(x, y):
    print(x + y)


# add(5, 5)


def decorator_1(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def decorator_2(func):
    def wrapper( *args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@decorator_1
@decorator_2
def add(x, y):
    print(x + y)

add(5, 5)

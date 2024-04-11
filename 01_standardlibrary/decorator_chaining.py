import time
import logging


def log_function(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with arguments {args} and keyword arguments {kwargs}')
        return func(*args, **kwargs)

    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {end - start:.6f} seconds to run')
        return result

    return wrapper


@log_function
@measure_time
def add(x, y):
    return x + y


# print(add(1, 2))


def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f'Error occurred in {func.__name__}: {e}')
    return wrapper


@handle_errors
def divide(x, y):
    return x / y


# print(divide(1, 0))

def bold(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return wrapper


def italic(func):
    def wrapper(*args, **kwargs):
        return f'<i>{func(*args, **kwargs)}</i>'
    return wrapper


@bold
@italic
def greet(name):
    return f'Hello, {name}'


print(greet('Alice'))
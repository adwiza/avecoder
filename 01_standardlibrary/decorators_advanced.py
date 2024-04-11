def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                func(*args, **kwargs)
        return wrapper
    return my_decorator


@repeat(num=3)
def greet(name):
    print(f'Hello, {name}!')


# greet('John')

def repeat(num, *, after=None, before=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if before is not None:
                before()
            for i in range(num):
                func(*args, **kwargs)
            if after is not None:
                after()
        return wrapper
    return my_decorator


def before_greeting():
    print("I'm doing something before the decorated function is called.")


def after_greeting():
    print("I'm doing something after the decorated function is called.")


@repeat(num=2, before=before_greeting, after=after_greeting)
def greet(name):
    print(f'Hello, {name}!')


# greet('John')

def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return my_decorator


def greet(name):
    print(f'Hello, {name}!')


greet_3_times = repeat(3)(greet)
greet_3_times('Alice')
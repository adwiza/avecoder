import time


# def log_execution_time(func):
#     def wrapper(self, *args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(self, *args, **kwargs)
#         end_time = time.perf_counter()
#         execution_time = end_time - start_time
#         print(f'{self.__class__.__name__}: {func.__name__} took {execution_time:.6f} seconds to execute')
#         return result
#     return wrapper
#
#
# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @log_execution_time
#     def add(self):
#         time.sleep(1)
#         return self.x + self.y
#
#
# calculator = Calculator(2, 3)
# result = calculator.add()
# print(result)

#########################
# def log_execution_time(cls):
#     class Wrapper(cls):
#         def __new__(cls, *args, **kwargs):
#             instance = super().__new__(cls)
#             instance.start_time = time.perf_counter()
#             return instance
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.end_time = time.perf_counter()
#             execution_time = self.end_time - self.start_time
#             print(f'{cls.__name__}: took {execution_time:.6f} seconds to instantiate')
#
#         def __del__(self):
#             end_time = time.perf_counter()
#             execution_time = end_time - self.start_time
#             print(f'{cls.__name__}: took {execution_time:.6f} seconds to be garbage collected')
#     return Wrapper
#
#
# @log_execution_time
# class Calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         time.sleep(1)
#
#     def add(self):
#         return self.x + self.y
#
#
# calculator = Calculator(2, 3)
# print(calculator.add())
class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Do something before
        print('John enters the room')
        result = self.func(*args, **kwargs)
        # Do something after
        print('John leaves the room')
        return result


@MyDecorator
def greet(name):
    print('Hello, ' + name + '!')


greet('John')

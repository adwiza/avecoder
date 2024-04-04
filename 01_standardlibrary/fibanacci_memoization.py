cache = {0: 0, 1: 1}


def fibonacci_mem(num):
    # base case
    if num in cache:
        return cache[num]
    # cache fib num
    cache[num] = fibonacci_mem(num - 1) + fibonacci_mem(num - 2)
    return cache[num]


if __name__ == '__main__':
    print([fibonacci_mem(num) for num in range(12)])
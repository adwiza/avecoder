import time


def main():
    start = time.perf_counter()

    a_list = [1, 2, 3, 4, 5]
    b_list = [6, 7, 8, 9, 10]
    c_list = []

    for a, b in zip(a_list, b_list):
        c_list.append(a * b)

    print(c_list)

    time.sleep(4)

    finish = time.perf_counter()

    print(f'Execution time: {finish - start:.4f} seconds')


if __name__ == '__main__':
    main()
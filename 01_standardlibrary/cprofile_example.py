import cProfile, pstats

# cProfile.run('20 * 110')


def create_array():
    arr = []
    for i in range(0, 500000):
        arr.append(i)


def print_statement():
    print('Array created successfully')


def main():
    create_array()
    print_statement()


if __name__ == '__main__':
    # cProfile.run('main()')
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')  # allows to change a sort order
    stats.print_stats()
    profiler.dump_stats('dump_stats')

    p = pstats.Stats('dump_stats')
    p.strip_dirs().print_stats()
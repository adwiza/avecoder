def my_function(arg1, arg2=None):
    """
    my_function(arg1, arg2=None) --> no purpose function
    :parameters
    :arg1 first argument, any type
    :arg2 second argument, defaults to None

    """
    print(arg1, arg2)


def main():
    print(my_function.__doc__)


if __name__ == '__main__':
    main()
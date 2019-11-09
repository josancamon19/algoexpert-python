def get_fib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1

    return get_fib(n - 2) + get_fib(n - 1)


if __name__ == '__main__':
    print(get_fib(6))

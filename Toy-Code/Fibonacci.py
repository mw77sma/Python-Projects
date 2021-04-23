import math


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fn1 = 0
    fn2 = 1

    for i in range(1, n):
        tmp = fn2
        fn2 = fn1 + fn2
        fn1 = tmp

    return fn2


if __name__ == '__main__':
    print(fibonacci(100))


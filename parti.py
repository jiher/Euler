class Memoize:

    """decorator to memoise a function"""

    def __init__(self, f):
        self.f = f
        self.cache = {}

    def __call__(self, *args):
        if not args in self.cache:
            self.cache[args] = self.f(*args)
        return self.cache[args]


@Memoize
def bigp(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    # run k from n to 1 to avoid excessive recursion depth
    return sum((-1) ** (k + 1) * (bigp(n - k * (3 * k - 1) / 2) + bigp(n - k * (3 * k + 1) / 2)) for k in range(n, 0, -1))

"""for n in range(10001):
    print n, bigp(n)
"""
print bigp(10000)
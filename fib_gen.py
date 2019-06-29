def fib_gen(times):
    x = 0; y = 1; count = 0
    while count < times:
        x, y = y, x + y
        yield x
        count += 1

for n in fib_gen(100):
    print(n)

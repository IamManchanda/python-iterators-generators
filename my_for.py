def my_for(iterable, func):
    my_iterator = iter(iterable)
    while True:
        try:
            my_iterations = next(my_iterator)
        except StopIteration:
            break
        func(my_iterations)

def my_square(x):
    print(x * x)

my_for("Hello", print)
my_for([1, 2, 3, 4, 5], my_square)

def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

my_gen = count_up_to(10)

print( next(my_gen) )

for num in my_gen:
    print(num)

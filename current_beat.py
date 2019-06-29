def current_beat():
    max = 100
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        yield nums[i]
        i += 1

print( current_beat() )

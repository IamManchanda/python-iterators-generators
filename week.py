def week():
    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    for day in days:
        yield day

my_gen = week()

while True:
        try:
            print( next(my_gen) )
        except StopIteration:
            break 


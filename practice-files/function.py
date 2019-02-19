def convert_to_seconds(day):
    hours = day * 24
    minutes = hours * 60
    seconds = minutes * 60

    return seconds


total_seconds = convert_to_seconds(7)

print(f'There are {total_seconds}')


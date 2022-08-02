numbers = (80, 90, 100)
iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

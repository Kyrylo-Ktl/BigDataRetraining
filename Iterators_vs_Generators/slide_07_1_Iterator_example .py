class PowersOfTwo:
    def __init__(self, max_power: int = 0):
        self.max_power = max_power
        self.power = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.max_power < self.power:
            raise StopIteration
        result = 2 ** self.power
        self.power += 1
        return result


powers = PowersOfTwo(10)
for value in powers:
    print(value)

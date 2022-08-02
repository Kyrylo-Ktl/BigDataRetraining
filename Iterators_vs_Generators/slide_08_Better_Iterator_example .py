class PowersIterator:
    def __init__(self, max_power: int):
        self.max_power = max_power
        self.curr_power = 0

    def __next__(self):
        if self.curr_power > self.max_power:
            raise StopIteration

        power = 2 ** self.curr_power
        self.curr_power += 1
        return power


class PowersOfTwo:
    def __init__(self, max_power: int = 0):
        self.max_power = max_power

    def __iter__(self):
        return PowersIterator(self.max_power)


powers = PowersOfTwo(10)
for value in powers:
    print(value)

for value in powers:
    print(value)

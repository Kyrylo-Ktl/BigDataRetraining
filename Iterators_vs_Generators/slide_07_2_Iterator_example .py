class PowersOfTwo:
    def __init__(self, max_power: int = 0):
        self.max_power = max_power

    def __getitem__(self, item):
        if item > self.max_power:
            raise StopIteration
        return 2 ** item


powers = PowersOfTwo(10)
for value in powers:
    print(value)

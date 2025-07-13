class JavaRandom:
    def __init__(self, seed):
        self.seed = (seed ^ 0x5DEECE66D) & ((1 << 48) - 1)

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return (self.seed >> (48 - bits)) & 0xFFFFFFFF

    def next_int(self, bound):
        if bound <= 0:
            raise ValueError("Bound must be positive")
        bits = self.next(31)
        return bits % bound
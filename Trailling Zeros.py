import math
class Tzero:
    def trailingZeroes(self, n: int) -> int:
        if n <= 0:
            return 0

        count, max_p = 0, int(math.log(n, 5))
        for i in range(1, max_p + 1):
            count += n // (5 ** i)

        return count

print(Tzero().trailingZeroes(5))
print(Tzero().trailingZeroes(3))
print(Tzero().trailingZeroes(0))

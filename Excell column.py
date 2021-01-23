class Excell:
    def convertToTitle(self, n: int) -> str:
        x = [chr(s) for s in range(ord('A'), ord('Z') + 1)]
        out = ""
        while n > 0:
            n -= 1

            n,i=n//26,n%26
            out += x[i]

        return out[::-1]
print(Excell().convertToTitle(289))
print(Excell().convertToTitle(1))
print(Excell().convertToTitle(25))
print(Excell().convertToTitle(87))
print(Excell().convertToTitle(704))
                
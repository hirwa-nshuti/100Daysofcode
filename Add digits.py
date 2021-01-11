class DigAdd:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        else:
            mod=(num-1)%9
            x =mod+1
            return x

print(DigAdd().addDigits(12))
print(DigAdd().addDigits(12836374))
print(DigAdd().addDigits(9))
print(DigAdd().addDigits(8))
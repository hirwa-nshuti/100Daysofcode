class PowerOfTwo:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n==1:
            return True
        while n%2==0:
            n=n/2
        return n==1


print(PowerOfTwo().isPowerOfTwo(181625276))
print(PowerOfTwo().isPowerOfTwo(3))
print(PowerOfTwo().isPowerOfTwo(9876))
print(PowerOfTwo().isPowerOfTwo(4))
print(PowerOfTwo().isPowerOfTwo(64))
print(PowerOfTwo().isPowerOfTwo(0))
print(PowerOfTwo().isPowerOfTwo(1))

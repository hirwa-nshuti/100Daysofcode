'''Write a function that takes an unsigned integer
 and returns the number of '1' bits it has (also known
  as the Hamming weight).

Note:

    Note that in some languages such as Java, there is 
     unsigned integer type. In this case, the input will 
     be given as a signed integer type. It should not affect 
     your implementation, as the integer's internal binary 
     representation is the same, whether it is signed or unsigned.
    In Java, the compiler represents the signed integers using 2's
     complement notation. Therefore, in Example 3 above, the input 
     represents the signed integer. -3.

Follow up: If this function is called many times, how would you
optimize it?'''

class Hamming:
    def hammingWeight(self, n: int) -> int:
        out = 0
        while n:
            n &= n - 1
            out += 1
        return out

if __name__=="__main__":
    a=111
    b=11
    c=1011
    print(Hamming().hammingWeight(a))
    print(Hamming().hammingWeight(b))
    print(Hamming().hammingWeight(c))

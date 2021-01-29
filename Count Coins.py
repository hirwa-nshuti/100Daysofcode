class Coins:
    def arrangeCoins(self, n: int) -> int:        
        out = int((n*2)**.5)
        if out*(out+1) > 2*n:
            return out - 1
        return out

if __name__=="__main__":
    a=12
    b=4
    c=92
    print(Coins().arrangeCoins(a))
    print(Coins().arrangeCoins(b))
    print(Coins().arrangeCoins(c))
class Recur:
    def fractionToDecimal(self, num: int, den: int) -> str:
        numerator=abs(num)
        denominator=abs(den)
        prev=numerator//denominator
        new=numerator%denominator
        if new==0:
            if (num*den)<0:
                return ("-"+str(prev))
            else:
                return (""+str(prev))
        fract=[]
        appearance={}
        shifts=0
        while(new not in appearance):
            if new !=0:
                appearance[new]=shifts
                fract.append(str((new*10)//denominator))
                new=(new*10)%denominator
                shifts+=1
            else:
                if(num*den)<0:
                    return ("-" + str(prev)+"."+"".join(fract))
                else:
                    return ("" + str(prev)+"."+"".join(fract))
        x=appearance[new]
        if (num*den)<0:
            return("-"+str(prev)+"."+"".join(fract[:x])+"("+"".join(fract[x:])+")")
        else:
            return(""+str(prev)+"."+"".join(fract[:x])+"("+"".join(fract[x:])+")")
if __name__=="__main__":
    a,b=2,3
    c,d=221,432
    print(Recur().fractionToDecimal(a,b))
    print(Recur().fractionToDecimal(c,d))
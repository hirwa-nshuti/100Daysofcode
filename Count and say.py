class Count:
    def countAndSay(self, n: int) -> str:
        cou='1'
        for i in range(n-1):
            j=0
            new_count=''
            while len(cou)>j:
                count=1
                while j<len(cou)-1 and cou[j]==cou[j+1]:
                    count+=1
                    j+=1
                j+=1
                new_count=new_count+str(count)+cou[j-1]
            cou=new_count
        return cou
a=12
b=1
c=8
print(Count().countAndSay(a))
print(Count().countAndSay(b))
print(Count().countAndSay(c))
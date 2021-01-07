class Plus:
    def plusOne(self, digits):
        i=len(digits)-1
        
        if digits=="":
            return 0

        while i>=0:
            added=digits[i]
            if(i==len(digits)-1):
                added+=1 
            if added<10:
                digits[i]=added
                return digits
                           
            elif added>=10 and i==0:
                digits[i]=0
                digits=[1]+ digits
            elif added>=10 and i>0:
                digits[i]=0
                digits[i-1]=digits[i-1]+1

                    
            i-=1
            
        return digits
if __name__ == "__main__":
    a=[1,2,3]
    print(Plus().plusOne(a))
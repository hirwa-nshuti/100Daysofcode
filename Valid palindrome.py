class ValidPalindrome:
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        else:
            s = "".join([i for i in s.lower() if i.isalnum()])
            i= 0 
            j=len(s)-1
            while j>i:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
                
        return True 

if __name__ == "__main__":
    a="A man, a plan, a canal: Panama"
    b="race a car"
    
    print(ValidPalindrome().isPalindrome(a))
    print(ValidPalindrome().isPalindrome(b))
    
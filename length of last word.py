class LastWord:
    def lengthOfLastWord(self, s: str) -> int:
        last=s.split()
        if len(last)==0:
            return 0
        while s:
            last_word=last[-1]
            x=len(last_word)
            if x==0:
                return 0
            else:
                return x
            break
        return x
a="Hello World"
b="      "
c="Hirwa    "
d=" Hi Felix how are you doing? "
print(LastWord().lengthOfLastWord(a))
print(LastWord().lengthOfLastWord(b))
print(LastWord().lengthOfLastWord(c))
print(LastWord().lengthOfLastWord(d))

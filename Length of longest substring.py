class Substring:
    def lengthOfLongestSubstring(s):
        first = []
        max_length = 0

        for x in s:
            if x in first:
                first = first[first.index(x)+1:]

            first.append(x)    
            max_length = max(max_length, len(first))
        return max(max_length,len(first))
print(Substring.lengthOfLongestSubstring("abcabcbb"))
print(Substring.lengthOfLongestSubstring("bbbbbbbbb"))
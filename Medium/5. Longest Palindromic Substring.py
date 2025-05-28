class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = []
        for i in range(len(s)):
            for j in range(len(s)-i):
                s1 = s[j:j+i+1]
                if s1[:] == s1[::-1]:
                    palindrome.append(s1)
        output = ''
        l = 0
        for i in palindrome:
            if len(i)>l:
                output = i
                l = len(i)                  
        return(output) 

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        if len(s) == 1:
            return s
        if len(set(s)) == 1:
            return s
        if s == s[::-1]:
            return s    
        max_palindrome_length = 0
        for i in range(len(s)):           
            if s[0:i+1] == s[0:i+1][::-1]:
                max_palindrome_length = i + 1       
        to_add = s[max_palindrome_length:][::-1]
        return to_add + s

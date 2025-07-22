class Solution:
    def makeFancyString(self, s: str) -> str:
        flag = 0
        new_str = s[0]
        for i in range(1,len(s)):
            new_str = new_str + s[i]
            if  s[i] == s[i-1]:
                flag += 1
            if s[i] != s[i-1]:
                flag = 0
            if flag == 2:
                flag -=1
                new_str = new_str[:-1]
        return new_str
            

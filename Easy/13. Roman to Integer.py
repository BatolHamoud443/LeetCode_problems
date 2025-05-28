class Solution:
    def romanToInt(self, s: str) -> int:
        s = s[::-1]
        m = 0
        for i in range(len(s)):
            if s[i] == 'I': m+=1
            elif s[i] == 'V': m+=5
            elif s[i] == 'X': m+=10
            elif s[i] == 'L': m+=50
            elif s[i] == 'C': m+=100
            elif s[i] == 'D': m+=500
            else : m+=1000                
            if i < len(s)-1:
                if s[i:i+2] == 'VI' or s[i:i+2] == 'XI': 
                    m-=2                    
                elif s[i:i+2] == 'LX' or s[i:i+2] == 'CX': 
                    m-=20                     
                elif s[i:i+2] == 'MC' or s[i:i+2] == 'DC': 
                    m-=200 

        return m

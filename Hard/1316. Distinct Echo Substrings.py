class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        sub = set()
        for i in range(len(text)):
            for j in range(i+1, len(text)):
                if text[i] == text[j]:
                    m = j-i
                    if text[i:i+m] == text[j:j+m]:        
                        sub.add(text[i:i+m])
        return len(sub)

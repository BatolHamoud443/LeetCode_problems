from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            num_words = j - i
            spaces_needed = maxWidth - line_len

            if j == n or num_words == 1:
            
                line = ' '.join(words[i:j])
                line += ' ' * (maxWidth - len(line))
            else:
                spaces = spaces_needed // (num_words - 1)
                extra = spaces_needed % (num_words - 1)

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    line += ' ' * (spaces + (1 if k - i < extra else 0))
                line += words[j - 1] 
            
            res.append(line)
            i = j
        
        return res


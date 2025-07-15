class Solution:
    def isValid(self, word: str) -> bool:
        v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if word.isalnum() == False:
            return False
        if len(word) >= 3:
            flag_vowel = False
            flag_constant = False

            for c in word:
                if c in v:
                    flag_vowel = True
                if c.isalpha() and c not in v:
                    flag_constant = True
                if flag_vowel and flag_constant:
                    return True
            if flag_vowel or flag_constant:
                    return False         
        else:
            return False

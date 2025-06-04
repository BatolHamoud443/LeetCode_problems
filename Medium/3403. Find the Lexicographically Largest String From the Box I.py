class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        largest_char = max(word)
        ind =  [index for index, char in enumerate(word) if char == largest_char]
        candidates = []
        for i in ind:
            if i >= numFriends-1:
                candidates.append(word[i:])
            else:
                candidates.append(word[i:i+1-numFriends])

        return max(candidates)
        

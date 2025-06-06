from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        result = []
        stack = []
        smallest = 'a'

        for c in s:
            stack.append(c)
            count[c] -= 1
            while smallest <= 'z' and count[smallest] == 0:
                smallest = chr(ord(smallest) + 1)
            while stack and stack[-1] <= smallest:
                result.append(stack.pop())

        return ''.join(result)


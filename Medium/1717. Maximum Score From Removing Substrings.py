class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def finder(s: str, flag: int, score: int):
            if flag == 0:
                a, b = 'a', 'b'
            else:
                a, b = 'b', 'a'

            stack = []
            count = 0
            for ch in s:
                if stack and stack[-1] == a and ch == b:
                    stack.pop()
                    count += score
                else:
                    stack.append(ch)
            return ''.join(stack), count

        if x > y:
            s_new, c1 = finder(s, 0, x) 
            _, c2 = finder(s_new, 1, y) 
        else:
            s_new, c1 = finder(s, 1, y)  
            _, c2 = finder(s_new, 0, x)  
        return c1 + c2


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a = ['0','1','2','3','4','5','6','7','8','9']
        m = len(num1)
        n = len(num2)
        first = 0
        for i in range(m):
            j = a.index(num1[i])
            first += j * 10**(m-i-1)

        second = 0
        for i in range(n):
            j = a.index(num2[i])
            second += j * 10**(n-i-1)

        return str(first * second)

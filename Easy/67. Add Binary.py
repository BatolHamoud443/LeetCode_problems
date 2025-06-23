class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_b = int(a, 2)
        b_b = int(b, 2)


        sum_binary = a_b + b_b

        return bin(sum_binary)[2:] 

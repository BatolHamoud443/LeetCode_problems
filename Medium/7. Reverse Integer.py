class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x == 0:
            return 0
        if x < 0:
            flag = 1
            x = -1*x
        x = str(x)
        x = x[::-1]
        while x[0] == '0':
            x = x[1:]
        if int(x) > 2147483647:
            return 0   
        if flag == 1:
            return -1*int(x)
        else:
            return int(x)

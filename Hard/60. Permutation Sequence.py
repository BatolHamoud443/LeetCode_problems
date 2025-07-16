class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        result = []
        while nums:
            index = k // factorial[n-1]
            if k % factorial[n-1] == 0:
                index -=1
            result.append(str(nums[index]))
            nums.pop(index)
            k = k - factorial[n-1]*index
            n = n-1
        
        return ''.join(result)

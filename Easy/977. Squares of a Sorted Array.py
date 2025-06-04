class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        m = -1
        if not nums:
            return []
        if nums[0] >= 0:
            return [n**2 for n in nums]
        for i in range(len(nums)):
            if nums[i] >= 0:
                m = i
                break
        if len(nums) == 1:
            return[nums[0]**2]
        if m == -1:
            return [n**2 for n in reversed(nums)]
            
        A = [n**2 for n in nums[m:]]
        B = [n**2 for n in reversed(nums[:m])]
        
        a, b = 0,0
        out = []
        while a < len(A) and b < len(B):
            if A[a] < B[b]:
                out.append(A[a])
                a +=1
            else:
                out.append(B[b])
            
                b +=1
        if a < len(A):
            out.extend(A[a:])
        else:
            out.extend(B[b:])
        return out

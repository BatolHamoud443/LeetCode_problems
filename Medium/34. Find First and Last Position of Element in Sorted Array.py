from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(arr, target):
            low, high = 0, len(arr) - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        k = binary_search(nums, target)
        if k == -1:
            return [-1, -1]
    
        l = k
        while l > 0 and nums[l - 1] == target:
            l -= 1
        r = k
        while r < len(nums) - 1 and nums[r + 1] == target:
            r += 1
        
        return [l, r]


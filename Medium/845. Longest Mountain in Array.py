class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        moun = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] > arr[i+1]:
                l = r = i
                while l > 0 and arr[l-1] < arr[l]:
                    l = l-1
                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r = r+1
                moun = max(moun, r-l+1)  
        return moun

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p_1 = 0
        p_2 = 0

        nums1[:] = nums1[:m]  

        while p_2 < n:
            if p_1 >= len(nums1):
                nums1.append(nums2[p_2])
                p_2 += 1
            elif nums1[p_1] <= nums2[p_2]:
                p_1 += 1
            else:
                nums1.insert(p_1, nums2[p_2])
                p_1 += 1
                p_2 += 1

        
        while len(nums1) < m + n:
            nums1.append(0)


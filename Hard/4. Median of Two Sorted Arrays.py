from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                if nums1 == []:
                    return median(nums2)
                elif nums2 ==[]:
                    return median(nums1)
                i = 0
                j = 0
                r = 0
                while i < len(nums2):
                    J = len(nums1)
            #         print(i)
                    if nums2[i] < nums1[j]:
                        nums1.insert(j,nums2[i])
                        i +=1
                    else: 
                        j +=1   
                    if j >= J:
                        nums1.append(nums2[i])
                        i +=1
            #         print(nums1)
                return median(nums1)

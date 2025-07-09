class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        startTime = [0] + startTime + [eventTime]
        endTime = [0] + endTime + [eventTime]

        slots = [startTime[i] - endTime[i-1] for i in range(1, len(endTime))]

        window_sum = sum(slots[:k+1])
        max_sum = window_sum    
        for i in range(k+1, len(slots)):
            window_sum += slots[i] - slots[i - (k+1)]
            max_sum = max(max_sum, window_sum) 
        return max_sum


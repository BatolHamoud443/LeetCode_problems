class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        i = 0
        curr = 1
        attended = 0
        min_heap = []
        while i < len(events) or len(min_heap) != 0:
            if not min_heap:
                curr = max(curr, events[i][0])     
            while i < len(events) and events[i][0] == curr:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            while min_heap and min_heap[0] < curr:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                attended += 1
            curr += 1
        
        return attended

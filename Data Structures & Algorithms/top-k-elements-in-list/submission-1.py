class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep a min heap, of len(nums)-k elements
        freqCount = Counter(nums)
        heap = []
        for num,count in freqCount.items(): # heaps compare with first element
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for count, num in heap]


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [num for num in nums]
        heapq.heapify(self.heap)
        self.k = k
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        print(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        print(self.heap)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        

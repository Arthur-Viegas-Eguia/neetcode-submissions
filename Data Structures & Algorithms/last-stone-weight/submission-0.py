class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stack = [-stone for stone in stones]
        heapq.heapify(stack)
        while len(stack) > 1:
            stone1, stone2 = -heapq.heappop(stack), -heapq.heappop(stack)
            resultingWeight = abs(stone1 - stone2)
            if resultingWeight > 0:
                heapq.heappush(stack, -resultingWeight)

        return -stack[0] if stack else 0
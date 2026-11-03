class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for point in points:
            dist.append([(point[0]**2 + point[1]**2), point])
        heapq.heapify(dist)
        res = []
        for i in range(k):
            res.append(heapq.heappop(dist)[1])
        return res
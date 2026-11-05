class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        totalWater = 0
        for h in range(1, len(height)):
            maxLeft[h] = max(height[h-1], maxLeft[h-1])
        maxRight = [0] * len(height)
        for h in range(len(height)-2, -1, -1):
            maxRight[h] = max(height[h+1], maxRight[h+1])
        for i in range(len(maxLeft)):
            totalWater += max(0, (min(maxRight[i], maxLeft[i]) - height[i]))
        return totalWater
        

        
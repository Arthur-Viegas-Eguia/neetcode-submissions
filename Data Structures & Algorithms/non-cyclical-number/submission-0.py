class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        n = str(n)
        if n == "1":
            return True
        while n not in seen and n != "1":
            seen.add(n)
            curr_sum = 0
            for digit in n:
                curr_sum += int(digit)**2
            n = str(curr_sum)
        return n == "1"

            
        
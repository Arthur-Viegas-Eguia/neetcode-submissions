class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        substr = set()
        l = 0
        for r in range(len(s)):
            while s[r] in substr:
                substr.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
            substr.add(s[r])
        return maxLen
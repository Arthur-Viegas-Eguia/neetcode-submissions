class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sLetters = [0] * 26
        tLetters = [0] * 26
        for i in range(len(s)):
            sLetters[ord(s[i]) - ord('a')] += 1
            tLetters[ord(t[i]) - ord('a')] += 1
        for i in range(26):
            if sLetters[i] != tLetters[i]:
                return False
        return True

        
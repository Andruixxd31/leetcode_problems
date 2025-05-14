class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        maxCount = 0
        count = 0
        l, r = 0, 0

        for r in range(k):
            if s[r] in vowels:
                count += 1

        maxCount = count 
        for r in range(k, len(s)):
            if s[l] in vowels:
                count -= 1
            l += 1
            if s[r] in vowels:
                count += 1
            maxCount = max(maxCount, count)

        return maxCount

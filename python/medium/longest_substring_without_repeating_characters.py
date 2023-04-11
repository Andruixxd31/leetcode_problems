class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniq = set()
        l = 0
        longest = 0
        for char in s:
            while char in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(char)
            longest = max(longest, len(uniq))
        return longest    

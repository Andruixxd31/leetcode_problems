class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.defaultdict(lambda:0)
        l = 0
        most_repeated_char = 0
        longest_sub = 0
        for r in range(len(s)):
            d[s[r]] += 1
            most_repeated_char = max(most_repeated_char, d[s[r]])  
            if (r - l + 1) - most_repeated_char > k:
                d[s[l]] -= 1
                l += 1
            longest_sub = max(longest_sub, r-l+1)
        return longest_sub

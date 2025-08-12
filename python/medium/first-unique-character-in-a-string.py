class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        unique = OrderedDict()
        for idx, char in enumerate(s):
            if char in seen:
                continue

            if char in unique:
                seen.add(char)
                del unique[char]
            else:
                unique[char] = idx

        return unique.popitem(last=False)[1] if len(unique) > 0 else -1

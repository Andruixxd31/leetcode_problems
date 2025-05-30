class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        lst = []
        count = 0
        for v in reversed(s):
            if v == "-":
                continue

            lst.append(v.upper())
            count += 1
            if count % k == 0:
                lst.append("-")

        if len(lst) > 0 and lst[-1] == "-":
            lst.pop()

        res = "".join(lst[::-1])
        return res

# start from the end, and reverse the4 string at the end
# so we can start by converting to upper and removing all dashes
# then, start at the end, and add that character. once we've reached k characters, set our ctr back to 0
# once we've reached the end, return our result

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        clean = s.replace("-", "").upper()
        res = []
        ctr = 0
        for idx, ch in enumerate(clean[::-1]):
            ctr += 1
            res.append(ch)
            if ctr == k and idx < len(clean) - 1:
                res.append("-")
                ctr = 0
            
        res.reverse()
        return "".join(res)

# starting from the left, if a number is greater than the number directly to the right of it, remove it
# continue doing this until we've either removed k elements or it's in non-descending order
#then, remove the rightmost number until we've reached k deletions
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        stack = []
        deletions = 0
        for idx, n in enumerate(num):
            as_i = int(n)
            while stack and as_i < stack[-1] and deletions < k:
                stack.pop()
                deletions += 1
            stack.append(as_i)
        final_len = len(num) - k
        stack = stack[:final_len]
        res =  "".join([str(s) for s in stack]).lstrip("0")
        if res == "":
            return "0"
        return res

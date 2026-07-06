class Solution:
    def maxValue(self, n: str, x: int) -> str:
        if n[0] == "-":
            neg = True
            n = n[1:]
        else:
            neg = False

        for idx in range(len(n)):
            cur = int(n[idx])
            if x > cur and not neg:
                return n[:idx] + str(x) + n[idx:]
            if x < cur and neg:
                return "-" + n[:idx] + str(x) + n[idx:]

                



        if neg:
            start = "-"
        else:
            start = ""
        return start + n + str(x)

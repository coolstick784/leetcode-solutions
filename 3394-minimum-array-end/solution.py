# 6 = 110
# 4 = 100
# 5 = 101


# 7 = 111
# 111
# 1111


# 0 0 0 0 0 0 0 0 0 0 

global two_pows
two_pows = [1]
for _ in range(100):
    two_pows.append(2*two_pows[-1])
two_pows.reverse()
# 1. convert n to binary
class Solution:


    def minEnd(self, n: int, x: int) -> int:
        global two_pows
        def get_binary(num):
            binary = []
            for p in two_pows:
                if num >= p:
                    num -= p
                    binary.append(1)
                else:
                    binary.append(0)
            return binary
        binary_n = get_binary(x)
        binary_x = get_binary(n-1)

        res = []
        x_idx = len(binary_x) - 1
        for idx in range(len(binary_n)-1, -1, -1):
            if binary_n[idx] == 0:
                res.append(binary_x[x_idx])
                x_idx -= 1
            else:
                res.append(1)


        res.reverse()
        out = 0
        for idx, p in enumerate(two_pows):
            if res[idx] == 1:
                out += p
        return out

waviness = []
for n in range(0, 10**5+1):
    as_l = [int(ch) for ch in str(n)]
    out = 0
    if len(as_l) >= 3:
        for idx in range(1, len(as_l) - 1):
            if (as_l[idx] < as_l[idx-1] and as_l[idx] < as_l[idx+1]) or (as_l[idx] > as_l[idx-1] and as_l[idx] > as_l[idx+1]):
                out += 1
    else:
        out = 0
    waviness.append(out)


# [1, 2, 1]

total = []
cur = 0
for w in waviness:
    cur += w
    total.append(cur)


# manually get waviness for each number in the range
# then, we want to get the total waviness up to and including num 2 - the total waviness of num1 - 1
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        end_2 = total[num2]
        if num1 == 1:
            end_1 = 0
        else:
            end_1 = total[num1-1]
        return end_2 - end_1

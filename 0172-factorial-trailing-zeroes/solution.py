# for every 10 there is a 0
# so we need to know the number of multiples of 10, as well as the number of multiples of (5*2)

number_10s = [0]
number_5s = [0]
number_2s = [0]
for n in range(1, 10**4+1):
    cur = n
    cur_n_10 = number_10s[-1]
    cur_n_5 = number_5s[-1]
    cur_n_2 = number_2s[-1]
    while cur % 10 == 0:
        cur_n_10 += 1
        cur //= 10
    while cur % 5 == 0:
        cur_n_5 += 1
        cur //= 5
    while cur % 2 == 0:
        cur_n_2 += 1
        cur //= 2
    number_10s.append(cur_n_10)
    number_5s.append(cur_n_5)
    number_2s.append(cur_n_2)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        return number_10s[n] + min(number_5s[n], number_2s[n])

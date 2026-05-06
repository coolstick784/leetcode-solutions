chars = [chr(ord('a') + n) for n in range(26)]

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        mag = [0 for _ in range(len(s) + 1)]

        for start, end, dn in shifts:
            if dn == 0:
                mag[start] -= 1
                mag[end + 1] += 1
            else:
                mag[start] += 1
                mag[end + 1] -= 1

        out = []
        cur_sum = 0

        for idx, c in enumerate(s):
            cur_sum += mag[idx]
            old_idx = ord(c) - ord('a')
            new_idx = (old_idx + cur_sum) % 26
            out.append(chr(ord('a') + new_idx))

        return "".join(out)

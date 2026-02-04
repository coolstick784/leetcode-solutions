from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = [0] * m
        start_r, start_c = startPos

        for i in range(m):
            r, c = start_r, start_c
            steps = 0

            for j in range(i, m):
                ch = s[j]
                if ch == 'L':
                    c -= 1
                elif ch == 'R':
                    c += 1
                elif ch == 'U':
                    r -= 1
                else:  # 'D'
                    r += 1

                # if out of bounds, stop
                if r < 0 or r >= n or c < 0 or c >= n:
                    break

                steps += 1

            ans[i] = steps

        return ans


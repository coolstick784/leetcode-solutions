# 1, 12, 13, 14, 17, 18, 20

class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        mx = stones[-1] - stones[1] - (len(stones) - 2)
        mx = max(mx, (stones[-2] - stones[0] - (len(stones) - 2)))

        mn = float('inf')
        for left_idx in range(len(stones)):
            right = stones[left_idx] + len(stones) - 1
            right_idx = bisect.bisect(stones, right) - 1

            if left_idx == 0 and right_idx == len(stones) - 2:
                if stones[right_idx] == right:
                    mn = 1
                continue

            if left_idx == 0 and right_idx == len(stones) - 1:
                if stones[right_idx] == right:
                    mn = 0
                continue
            if right > stones[-1]:
                continue


            cur_inside = right_idx - left_idx + 1

            to_move = len(stones) - cur_inside
        
            mn = min(mn, to_move)

        return [mn, mx]

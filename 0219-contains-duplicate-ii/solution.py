class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ctr = {}
        for idx, n in enumerate(nums):
            ctr.setdefault(n, []).append(idx)
        for n in ctr:
            for idx_idx, idx in enumerate(ctr[n]):
                if idx_idx == 0:
                    continue
                if idx - ctr[n][idx_idx-1] <= k:
                    return True
        return False

from typing import List
from collections import Counter
import heapq

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        if len(nums) == 1:
            return (nums[0] + k) % MOD

        ctr = Counter(nums)
        heap = list(ctr.keys())
        heapq.heapify(heap)

        while k > 0:
            # pop until we find a value that still exists (count > 0)
            while heap and ctr[heap[0]] == 0:
                heapq.heappop(heap)
            if not heap:
                break

            low = heapq.heappop(heap)
            low_count = ctr[low]
            if low_count == 0:
                continue  # safety

            # next distinct value (or "infinity" if none)
            while heap and ctr[heap[0]] == 0:
                heapq.heappop(heap)
            next_val = heap[0] if heap else float("inf")

            if next_val == float("inf"):
                # no higher value to catch up to: just distribute k over this bucket
                add = k // low_count
                rem = k % low_count

                ctr[low] = 0
                ctr[low + add] += (low_count - rem)
                ctr[low + add + 1] += rem

                # push the new keys we created
                heapq.heappush(heap, low + add)
                if rem:
                    heapq.heappush(heap, low + add + 1)
                k = 0
            else:
                # cost to raise all lows up to next_val
                gap = next_val - low
                cost = low_count * gap

                if cost <= k:
                    # raise entire bucket to next_val and merge
                    k -= cost
                    ctr[low] = 0
                    ctr[next_val] += low_count
                    # next_val is already in heap (as a key), no need to push it
                else:
                    # can't fully reach next_val: raise partially within bucket
                    add = k // low_count
                    rem = k % low_count

                    ctr[low] = 0
                    ctr[low + add] += (low_count - rem)
                    ctr[low + add + 1] += rem

                    heapq.heappush(heap, low + add)
                    if rem:
                        heapq.heappush(heap, low + add + 1)
                    k = 0

        # product mod MOD (fast)
        res = 1
        for val, count in ctr.items():
            if count > 0:
                res = (res * pow(val, count, MOD)) % MOD
        return res


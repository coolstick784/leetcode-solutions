# in both: yes -> no -> yes -> no -> ...
# in val but not k: yes -> yes -> yes -> ....
# in k but not val: no -> yes -> no -> yes...
# in neihter: no -> no....


# we can either swap an odd or even number of connections for each node
# we want to find the max value if we swap an odd number, as well as the max value if we swap an even number
# assume everything is swap, then unswap each one, and get the max

import heapq
from collections import deque
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        conns = {}
        for start, end in edges:
            conns.setdefault(start, set()).add(end)
            conns.setdefault(end, set()).add(start)

        turned_on = [False for _ in nums]
        @lru_cache(None)
        def dfs(node, start = False, prev = None):
            cur = conns.get(node, set())
            xor = nums[node] ^ k
            no_xor = nums[node]
            cur_sum = 0 # how much if we don't swap
            cur_diffs = [] # difference sorted highest to lowest (how much to the sum we would add if we swap)
            if len(cur) < 1 or (len(cur) == 1 and next(iter(cur)) == prev):
                return nums[node] ^ k if start else nums[node]
            for conn in cur:
                if conn == prev:
                    continue
                no_swap = dfs(conn, False, node)
                swap = dfs(conn, True, node)
                cur_sum += no_swap
                heapq.heappush(cur_diffs, -(swap-no_swap))

            if start:
                base = xor
            else:
                base = no_xor
            out = cur_sum + base
            while cur_diffs:
                if base == no_xor:
                    base = xor
                else:
                    base = no_xor
                to_add = -heapq.heappop(cur_diffs)
                cur_sum += to_add
                out = max(out, cur_sum + base)
            return out



        return dfs(0)

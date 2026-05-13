# we'll have a heap, each el will be (char, -idx) because we want to pop the rightmost
# we'll have a set of to remove idxs


class Solution:
    def clearStars(self, s: str) -> str:
        to_remove = set()
        heap = []
        for idx, ch in enumerate(s):
            if ch == "*":
                to_remove.add(idx)
                to_remove.add(-heapq.heappop(heap)[1])
            else:
                heapq.heappush(heap, (ch, -idx))
        res= []
        for idx, ch in enumerate(s):
            if idx not in to_remove:
                res.append(ch)
        return "".join(res)

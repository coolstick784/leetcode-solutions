class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        mp = {}
        for idx, p in enumerate(people):
            mp.setdefault(p, []).append(idx)
        people.sort()
        flowers.sort()
        flowers = deque(flowers)
        ends = []
        res = [None for _ in people]
        for p in people:
            while flowers and p >= flowers[0][0]:
                start, end = flowers.popleft()
                heapq.heappush(ends, end)
            while ends and p > ends[0]:
                heapq.heappop(ends)
            res[mp[p].pop()] = len(ends)
        return res

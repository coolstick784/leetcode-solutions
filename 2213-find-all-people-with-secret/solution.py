class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        edges = {}
        for x, y, time in meetings:
            edges.setdefault(x, []).append((y, time))
            edges.setdefault(y, []).append((x, time))

        heap = [(0, 0), (0, firstPerson)]  # time, person
        res = set()

        while heap:
            time, person = heapq.heappop(heap)

            if person in res:
                continue

            res.add(person)

            for nei, t in edges.get(person, []):
                if t >= time:
                    heapq.heappush(heap, (t, nei))

        return list(res)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pres = {}
        ends = {}
        for end, start in prerequisites:
            pres.setdefault(start, set()).add(end)
            ends.setdefault(end, set()).add(start)
        can_do = deque([n for n in range(numCourses) if n not in ends])
        res = []
        while can_do:
            course = can_do.popleft()
            res.append(course)
            for end in pres.get(course, []):
                ends[end].remove(course)
                if not ends[end]:
                    can_do.append(end)



        if len(res) == numCourses:
            return res
        return []

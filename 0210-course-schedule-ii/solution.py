from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        explored = set()
        add = deque()
        res = []
        need = {}
        is_needed = {}
        total = set()
        for c, b in prerequisites:
            need.setdefault(c, set()).add(b)
            is_needed.setdefault(b, set()).add(c)
            total.add(c)
            total.add(b)
        for p in range(numCourses):
            if len(need.get(p, set())) == 0:
                add.append(p)
        while add:
            c = add.popleft()
            explored.add(c)
            for c2 in is_needed.get(c, set()):
                if c2 in explored:
                    continue
                need[c2].remove(c)
                if len(need[c2]) == 0:
                    add.append(c2)
            res.append(c)
        if len(res) != numCourses:
            return []
        return res

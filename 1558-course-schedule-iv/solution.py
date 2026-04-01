class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create a LRU cache function that returns whether or not a course is a prereq of another
        # Create a dict with all prereqs needed for a course
        # In the function, have a recursive loop that goes through all prereqs

        prereq_dict = {}
        for pre, out in prerequisites:
            prereq_dict.setdefault(out, [])
            prereq_dict[out].append(pre)
        
        @lru_cache(None)
        def find_prereq(inp, out):
            if out not in prereq_dict:
                return False
            if True in [find_prereq(inp, last) for last in prereq_dict[out]]:
                return True
            if inp in prereq_dict[out]:
                return True
            return False
        
        res = []
        for inp, out in queries:
            if find_prereq(inp, out):
                res.append(True)
            else:
                res.append(False)
        return res
        

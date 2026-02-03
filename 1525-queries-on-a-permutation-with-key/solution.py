class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        perm = list(range(1, m + 1))
        answer = []
        for q in queries:
            idx = perm.index(q)
            answer.append(idx)
            perm.pop(idx)
            perm.insert(0, q)
        return answer

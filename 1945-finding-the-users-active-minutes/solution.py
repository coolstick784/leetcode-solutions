class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        users = {}

        res = {}
        for user, m in logs:
            users.setdefault(user, set()).add(m)
        for u in users:
            v = len(users[u])
            res[v] = res.get(v, 0) + 1
        final = []
        for idx in range(1, k+1):
            final.append(res.get(idx, 0))
        return final


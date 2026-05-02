# if either:
# it's the first player, and they're better than their k next opponents or
# 
class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        sol = [0, 0]
        players = deque([n for n in range(len(skills))])
        cur = players.popleft()
        m = max(skills)
        while sol[1] < k:
            if skills[cur] == m:
                return cur
            if skills[cur] > skills[players[0]]:
                players.append(players.popleft())
                sol[1] += 1
            else:
                players.append(cur)
                cur = players.popleft()
                sol[0] = cur
                sol[1] = 1

        return sol[0]



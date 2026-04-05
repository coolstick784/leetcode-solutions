class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = set()
        lost_two_more = set()
        for winner, loser in matches:
            winners.add(winner)
            if winner in losers or winner in lost_two_more:
                winners.remove(winner)
            if loser in winners:
                winners.remove(loser)
            if loser in losers:
                losers.remove(loser)
                lost_two_more.add(loser)
            elif loser in lost_two_more:
                pass
            else:
                losers.add(loser)
        return [sorted(list(winners)), sorted(list(losers))]


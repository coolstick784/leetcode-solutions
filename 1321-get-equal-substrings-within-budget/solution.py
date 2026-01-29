class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = []
        cur_max = 0
        left = 0
        for idx, ch1 in enumerate(s):
            ch2 = t[idx]
            cur_cost = abs(ord(ch2) - ord(ch1))
            if costs == []:
                costs = [cur_cost]
            else:
                costs.append(costs[-1] + cur_cost)
        print(costs)
        for idx, cost in enumerate(costs):
           
            if cost <= maxCost:
                cur_max = max(cur_max, idx+1)

            for att in costs[left:idx]:
                if (cost - att) <= maxCost:
                    cur_max = max(cur_max, idx - left)
                    break
                left += 1
        return cur_max


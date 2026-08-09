class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        sum_wait = 0
        cur_time = 0
        for a, t in customers:
            cur_time = max(cur_time, a)
            cur_time += t
            sum_wait += (cur_time - a)
        return sum_wait / len(customers)

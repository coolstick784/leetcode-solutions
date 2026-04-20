# at each station, we want to know the following:
# how much gas would we need to start with to get to the last station from this station, and how much gas would we have left?
# from the last station, how much gas would we need to get to this station?
# then, if our starting gas is >= the start, and the gas left at the end is >= the amount needed to get there, return that
# do this for each index
# if it doesn't work, return -1
# to calculate how much gas we need to get from the last station to this station, we can start at the end
# so if we get to an index, and cost > gas, we need max_cost + cost-gas
# if cost = gas, retain our max_cost
# if cost < gas, we need max(0, max_cost +cost-gas)


# then, from the first to this station, we need to work forward
# if cost > gas, we need max_cost + cost-gas
# if cost = gas, retain max_cost
# if cost < gas, we need max_cost + cost-gas


# 1. can we get to the end starting with this index?
# 2. if so, how much gas will we be left with?
# 3. how much gas will we need if, starting at the last index, we get back to our current index?
# 4. if 1, and 2 >= 3, return idx
# otherwise, move to the next

# for 1, we want to ask: how much excess is needed to get to this point, and do we have that excess?
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] >= cost[0]:
                return 0
            else:
                return -1
        excess = [0 for _ in range(len(cost))]
        can_end = [True for _ in range(len(cost))]
        left_at_end = [0 for _ in range(len(cost))]
        
        cur_cost = 0
        for idx in range(len(cost) - 2, -1, -1):
            cost_idx = cost[idx]
            gas_idx = gas[idx]
            excess[idx] = max(0, excess[idx+1] + cost_idx - gas_idx)
            left_at_end[idx] = left_at_end[idx+1] + gas_idx - cost_idx
            if excess[idx] != 0:
                can_end[idx] = False 


        cost_to_get = cost[-1] - gas[-1]
        for idx in range(len(gas)):

            cost_idx = cost[idx]
            gas_idx = gas[idx]

            if left_at_end[idx] >= cost_to_get and can_end[idx]:
                return idx

            cost_to_get += (cost[idx] -gas[idx])
            
            
        return -1



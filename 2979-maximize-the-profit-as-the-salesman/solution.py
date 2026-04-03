# Sort the starting points in order
# For each offer, we can ask: what's the best offer up until this point? and add that value to it
# Then, update the ending point to be the max of offer + sum up till offer, current value
# To find the best offer, we need an algorithm to determine the highest offer before that starting index
# if an index is populated, we can say that value is the highest value up to and including that index
# we can give a list of indices that have been populated
# then, we use binary search/bisect to find the first index before the current index, and we use that score to get the best score up to that point

# we know we want to only look through the values that are between the last start and the new start -1, inclusive
# we need to know the index in best 

class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        start_dict = {}
        starts = []
        for start, end, gold in offers:
            start_dict.setdefault(start, []).append([end, gold])
            starts.append(start)
        starts = list(set(starts))
        starts.sort()

        best = [0 for _ in range(n+1)]
        cur_best_idx = 0

        for start in starts:

            
            
            if start == starts[0]:
                cur_best = 0
            else:
                cur_best = max(best[max(prev_start-1, 0):start])
                best[start-1] = cur_best

            prev_start = start


            
            for end, gold in start_dict[start]:


                best[end] = max(best[end], cur_best+gold)

  
        return max(best)

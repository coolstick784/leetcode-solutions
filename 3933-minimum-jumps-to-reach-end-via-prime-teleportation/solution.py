primes = [True for _ in range(10**6+1)]
primes[0] = False
primes[1] = False
max_val = 10**6
all_p = set()
for idx, p in enumerate(primes):
    if p:
        all_p.add(idx)
        cur = idx + idx
        while cur <= max_val:
            primes[cur] = False
            cur += idx



# what we can do is start at 0
# for n+1, n-1, and every multiple, we can add it to explored if it's valid and not in explored. also add it to to_explore
# then, for each in to_explore, we do the same thing
# repeat until we reach n-1

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        explored = set([0])
        to_explore = deque([(0, 0)])
        res = 0
        max_n = max(nums)
        idx_dict = {}
        for idx, n in enumerate(nums):
            idx_dict.setdefault(n, []).append(idx)


        while to_explore:
            idx , res = to_explore.popleft()
    
            if idx == len(nums) - 1:
                return res
            if nums[idx] in all_p:
                cur = nums[idx]
                while cur <= max_n:
                    for p in idx_dict.get(cur, []):
                        if p not in explored and nums[p] % nums[idx] == 0:
                            explored.add(p)
                            to_explore.append((p, res+1))
                        if cur in idx_dict:
                            del idx_dict[cur]



                    cur += nums[idx]

                    
            
            if idx-1 >= 0 and idx-1 not in explored:
                explored.add(idx-1)
                to_explore.append((idx-1, res+1))
            if idx+1 not in explored:
                explored.add(idx+1)
                to_explore.append((idx+1, res+1))


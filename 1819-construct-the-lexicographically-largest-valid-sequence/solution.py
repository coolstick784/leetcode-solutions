from collections import deque
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        

        res = [None for _ in range(n*2-1)]

        @lru_cache(None)
        def possible(given):
            
            nonlocal n
            nonlocal res
            explored = set()
            idxs = []
            cur = [None for _ in range(n*2-1)]
            print("given", given, "cur", cur)
            for num, idx, idx2 in given:
                cur[idx] = num
                cur[idx2] = num
                explored.add(num)
            print("cur", cur)
            stack = []
            for num in range(1, n+1):
                if num not in explored:
                    stack.append(num)
            print("stack", stack)
            for idx in range(n*2-1):
                if cur[idx] is None:
                    first_idx = idx
                    break
            if not stack:
                res= cur.copy()
                
                return True
            
            new_given = {}
            for num, idx, idx2 in given:
                new_given[num] = [idx, idx2]
            while stack:
                num = stack.pop()
                print("n", num)
                if num == 1 or (first_idx + num < len(cur) and cur[first_idx + num] is None):
                    cur[first_idx] = num
                    if num != 1:
                        cur[first_idx+num] = num
                        new_given[num] = [first_idx, first_idx+num]
                    else:
                        new_given[num] = [first_idx, first_idx]
                    ret = []
                    for num2 in new_given:
                        ret.append((num2, new_given[num2][0], new_given[num2][1]))
                    ret.sort()
                   
                    if possible(tuple(ret)):
                        return True
                    cur[first_idx] = None
                    cur[first_idx+num] = None
                    del new_given[num]
            return False

                    
                    
            



        possible(tuple([]))
        return res

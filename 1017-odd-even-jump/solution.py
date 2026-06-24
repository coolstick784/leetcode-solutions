# can we get to each index, ending with an odd jump or even jump?
# so we want to keep track of the number of jumps we have

from collections import OrderedDict
class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        canEven = set()
        canOdd = set()
        nextEven = {}
        nextOdd = {}

        def trace(cur, l):
            if l[cur] == cur:
                return cur
            l[cur] = trace(l[cur], l)
            return l[cur]

        def merge(prev, new, l):
            if new not in l:
                l[prev] = -1
                return
                
            l[prev] = trace(new, l)
   

        rest = OrderedDict()
        idxs = {}
        for idx, n in enumerate(arr):
            idxs.setdefault(n, deque()).append(idx)
        keys = sorted(list(idxs.keys()))
        key_idxs = {}
        unionOdd = {}
        unionEven = {}
        unionOdd[-1] = -1
        unionEven[-1] = -1

        for idx, n in enumerate(keys):
            key_idxs[n] = idx
            unionOdd[n] = n
            unionEven[n] = n
        

        for idx, n in enumerate(arr):
            idxs[n].popleft()
            if not idxs[n]:
                del idxs[n]
                key_idx = key_idxs[n]
                if key_idx > 0:
                    merge(n, keys[key_idx-1], unionEven)
                else:
                    unionEven[n] = -1
                if key_idx < len(keys) - 1:
                    merge(n, keys[key_idx+1], unionOdd)
                else:
                    unionOdd[n] = -1
            
            evenIdx = idxs.get(unionEven[n], [-1])[0]
            oddIdx = idxs.get(unionOdd[n], [-1])[0]

            nextEven.setdefault(evenIdx, set()).add(idx)
            nextOdd.setdefault(oddIdx, set()).add(idx)
            
                



        print("next odd", nextOdd, "enxt even", nextEven)
        canEven.add(len(arr) - 1)
        canOdd.add(len(arr) - 1)
        for idx in range(len(arr) -1, -1, -1):
            if idx in canEven:
                for prev in nextOdd.get(idx, set()):
                    canOdd.add(prev)
            if idx in canOdd:
                for prev in nextEven.get(idx, set()):
                    canEven.add(prev)

        res = set()
        res.add(len(arr) - 1)
        for idx in canEven:
            for prev in nextOdd.get(idx, set()):
                res.add(prev)
        print("caneven", canEven, "can odd", canOdd)
        return len(res)
            

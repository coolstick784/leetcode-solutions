class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # for each path, list its connections
        # start by defining the first value as 1
        # for each of the connections of the first garden, try each flower 1-4. expand from those gardens
        # if no flowers work, change the level it comes from and try again
        # once a garden is complete, try all other gardens until you're finished

        # Get the order in which we want to go, so if one fails, we go back and try another one 

        # 1. Go from 1->2->3->1
        # 2. At 2, try 2 because it's not in 1 or 3

        if paths == []:
            return [1 for i in range(1, n+1)]

        paths_dict = {}
        for s, e in paths:
            paths_dict.setdefault(s, []).append(e)
            paths_dict.setdefault(e, []).append(s)

        
        res = [None for _ in range(n+1)]
        order = []
        explored = set()
        print("paths dict", paths_dict)
        for i in range(1, n+1):
            if i not in explored:
                order.append(i)
                explored.add(i)
                if i not in paths_dict:
                    continue
                poss = [j for j in paths_dict[i] if j not in explored]
                while poss != []:
                    order.append(poss[0])
                    explored.add(poss[0])
                    poss = [j for j in paths_dict[poss[0]] if j not in explored]
        
        order_idx = 0
                    
        while order_idx < len(order):
            n = order[order_idx]
            if res[n] != None:
                res[n] += 1
            else:
                if n not in paths_dict:
                    res[n] = 1
                    order_idx += 1
                    continue
                others = [res[i] for i in paths_dict[n]] 
                pot = [i for i in range(1, 6) if i not in others ]
                res[n] = min(pot)
            if res[n] == 5:
                res[n] = None
                order_idx -= 1
            else:
                order_idx += 1


        return res[1:]


        

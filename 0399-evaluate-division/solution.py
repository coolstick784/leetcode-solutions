class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        a = {}

        letters = set()
        for start, end in equations:
            letters.add(start)
            letters.add(end)
        letters = list(letters)
        combos = []
        for letter in letters:
            for l2 in letters:
                combos.append((letter, l2))
        for l1, l2 in combos:
            a[(l1, l2)] = float(-1)
        for idx, (n, d) in enumerate(equations):
            a[(n, d)] = values[idx]
            a[(d, n)] = 1/values[idx]
        explored = 1
        while explored > 0:
            explored = 0
            
            for idx, (l1, l2) in enumerate(combos):
                if a[(l1, l2)] == float(-1):
                    continue
                a[(l2, l2)] = 1
                pot = [(l2, new) for new in letters]
                for l3, l4 in pot:
                    if l3 == l2 and a[(l3, l4)] != -1 and a[(l1, l4)] == -1:
                        explored += 1
                        a[(l1, l4)] = a[(l1, l2)] * a[(l3, l4)]
  
        ans = []
        for l1, l2 in queries:
            ans.append(a.get((l1, l2), -1))
        return ans




                

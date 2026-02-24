class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        # There are 2^6 = 64 possible combinations
        # 1. get where it's at on day one
        # 2. find the # of days it takes to cycle
        # 3. print the modulus it's on after cycling
        
        def makeDayOne(cells):
            out = []
            for idx, n in enumerate(cells):
                if idx == 0 or idx == len(cells) - 1:
                    out.append(0)
                elif cells[idx-1] == cells[idx+1]:
                    out.append(1)
                else:
                    out.append(0)
            return out
        
        def findCycleDays(dayOne):
            cycles = [dayOne]
            cur = dayOne.copy()
            ctr = 0
            while cur != dayOne or ctr == 0:
                ctr += 1
                out = []
                for idx, n in enumerate(cur):
                    if idx == 0 or idx == len(cur) - 1:
                        out.append(0)
                    elif cur[idx-1] == cur[idx+1]:
                        out.append(1)
                    else:
                        out.append(0)   
                cycles.append(out)
                cur = out.copy()

            cycles.pop()
            
            return cycles
        
        
        
        
        dayOne = makeDayOne(cells)
        if n == 1:
            return dayOne

        cycles = findCycleDays(dayOne)

        return cycles[(n - 1) % len(cycles)]
        

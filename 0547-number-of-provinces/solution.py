class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Look at each connection, and then set the property blank after looking through it
        # Look at 1 -> 2 and set the connection from 1 to 2 to null both ways, then look at 2-> anything else, and so on
        # Then look at the connections from 2, and keep going until we reach the end

        res = 0
        no_conns = [0 for _ in range(len(isConnected[0]))]
        conns = set()

        def connectProvinces(r):
            cur_row = isConnected[r]
            for idx, el in enumerate(cur_row):
                if el == 1:
                    conns.add(idx)
                    isConnected[r][idx] = 0
                    isConnected[idx][r] = 0
                    connectProvinces(idx)




        for r in range(len(isConnected)):
            isConnected[r][r] = 0
        for r in range(len(isConnected)):
            if r not in conns:
                res += 1
                conns.add(r)
                connectProvinces(r)


        return res
            


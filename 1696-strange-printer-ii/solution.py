from collections import deque

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        find = {}
        beforeThis = {}
        afterThis = {}
        q = deque()
        
        for r, row in enumerate(targetGrid):
            for c, el in enumerate(row):
                find.setdefault(el, {})
                find[el]['left'] = min(find[el].get('left', float('inf')), c)
                find[el]['right'] = max(find[el].get('right', 0), c)
                find[el]['down'] = max(find[el].get('down', 0), r)
                find[el]['up'] = min(find[el].get('up', float('inf')), r)

        num_colors = len(find)

        for color in find:
            l = find[color]['left']
            r = find[color]['right']
            u = find[color]['up']
            d = find[color]['down']

            afterThis.setdefault(color, set())

            for rn in range(u, d + 1):
                for c in range(l, r + 1):
                    el = targetGrid[rn][c]

                    if el == color:
                        continue

                    beforeThis.setdefault(el, set()).add(color)
                    afterThis[color].add(el)

        for color in find:
            if color not in beforeThis:
                q.append(color)

        while q:
            color = q.popleft()
            num_colors -= 1

            for conn in afterThis[color]:
                beforeThis[conn].remove(color)

                if not beforeThis[conn]:
                    q.append(conn)

        return num_colors == 0

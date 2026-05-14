class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = {}
        items = set()
        tables_list = set()
        for name, table, order in orders:
            tables.setdefault(table, {})
            tables[table][order] = tables[table].get(order, 0) + 1
            items.add(order)
            tables_list.add(int(table))
        items = sorted(list(items))
        tables_list = sorted(list(tables_list))
        res = []
        display = ["Table"]
        display += items
        res.append(display)
        for t in tables_list:
            table = str(t)
            cur = [table]
            for item in items:
                cur.append(str(tables[table].get(item, 0)))
            res.append(cur)
        return res
            

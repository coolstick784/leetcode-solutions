# first, convert the transactions to 4 vars
# we want a dict, with the key being the name and the values being a list of tuples with time and city
# we can have another dict that maps said tuples to their strings
# for each transaction, find each other transaction from that name that is within 60 minutes and in another city, and remove them both
# obviously if amount exceeds 1k remove that 

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        names = {}
        map_dict = {}
        res = set()
        for idx, t in enumerate(transactions):
            name, time, amt, city = t.split(",")
            time = int(time)
            amt = int(amt)
            if amt > 1000:
                res.add((t, idx))
            names.setdefault(name, []).append((name, time, amt, city))
            map_dict.setdefault((name, time, amt, city), []).append((t, idx))
            for p_name, p_time, p_amt, p_city in names[name]:
                if abs(time - p_time) <= 60 and city != p_city:
                    res.add((t, idx))
                    for s, idx2 in map_dict[(p_name, p_time, p_amt, p_city)]:
                        res.add((s, idx2))
                    
        
        out = []
        for s in res:
            out.append(s[0])
        return out

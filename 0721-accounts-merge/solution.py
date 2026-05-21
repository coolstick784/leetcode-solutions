class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union_find = [idx for idx in range(len(accounts))]
        emails = {}
        def place_union(n1, n2):
            if union_find[n1] == n1 and union_find[n2] == n2:
                union_find[n2] = n1
                return 
            prev = union_find[n2]
            union_find[n2] = n1
            place_union(n1, prev)
            return 
        for idx, acc in enumerate(accounts):
            for email in acc[1:]:
                emails.setdefault(email, []).append(idx)

        for email in emails:
            cur = emails[email]
            if len(cur) >= 2:
                for idx in range(1, len(cur)):
                    place_union(cur[idx-1], cur[idx])
        
        out = {}
        print(emails)
        
        def trace_union(n):
            if union_find[n] == n:
                return n
            return trace_union(union_find[n])
        for i, idx in enumerate(union_find):
            union_find[i] = trace_union(idx)
        print(union_find)

        
        for og, idx in enumerate(union_find):
            out.setdefault(idx, [None])
            out[idx][0] = accounts[og][0]
            out[idx] += accounts[og][1:]
        for idx in out:
            out[idx] = [out[idx][0]] + sorted(list(set(out[idx][1:])))
        return list(out.values())


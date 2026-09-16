class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        ctr = {}
        for d in cpdomains:
            ct, url = d.split()
            ct = int(ct)
            subs = url.split(".")
            cur = ""
            for d in subs[::-1]:
                if cur:
                    cur = d + "." + cur
                else:
                    cur = d
                ctr[cur] = ctr.get(cur, 0) + ct
                
        res = []
        for s, ct in ctr.items():
            res.append(str(ct) + " " + s)
        return res


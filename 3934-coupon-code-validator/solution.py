class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        lists = {
            'electronics':[],
            'grocery':[],
            'pharmacy':[],
            'restaurant':[]
        }
        res = []

        businesses = ['electronics', 'grocery', 'pharmacy', 'restaurant']
        for idx, c in enumerate(code):
            business = businessLine[idx]
            active = isActive[idx]
            isalnum = False
            if len(c) > 0 and c.replace("_", "") == "":
                isalnum = True
            elif len(c) > 0 and c.replace("_", "").isalnum():
                isalnum = True
            if  isalnum and business in businesses and active:
                lists[business].append(c)
        for l in lists:
            lists[l].sort()
            res += lists[l]
        return res

        

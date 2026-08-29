class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        vals = {}
        for p in paths:
            files = p.split()
            root = files[0]
            
            for file in files[1:]:
                path = []
                content = []
                found_p = False
                for idx, ch in enumerate(file):
                    if not found_p and ch != "(":
                        path.append(ch)
                    elif ch == r"(":
              
                        found_p = True
                        path = root + "/" + "".join(path)
                    elif ch != r")":
                        content.append(ch)
                content = "".join(content)
             
                
                vals.setdefault(content, []).append(path)
        
        res = []
        for v in vals:
            if len(vals[v]) > 1:
                res.append(vals[v])
        return res

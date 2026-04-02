class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # sliding window
        # left dot starting right after 0, second dot right after the first, and so on
        # keep moving the rightmost dot until the right is valid
        # then the second to right dot until the second to last is valid
        # ... and so on until we have a valid ip address
        # then, move the right dot one and so on
        # if two dots are overlapping, or if the right is past the end, return what we have
        self.res = []

        def isValid(n):
            if n == "" or len(n) > 3 or int(n) < 0 or int(n) > 255:
                return False
            if n.startswith("0") and len(n) > 1:
                return False
            return True
        @lru_cache(None)
        def solve(sub, dots, cur):
            print("sub", sub, "dots", dots, "cur", cur)
            if dots == 0 and isValid(sub):
                self.res.append(cur + "." + sub)
                return 
            if dots == 0 and not isValid(sub):
                return
            valid = []
            # valid can be 1, 2, 3
            for i in range(1, 4):
                if isValid(sub[:i]):
                    if cur == "":
                        new = sub[:i]
                    else:
                        new = cur + "." + sub[:i]
    
                    solve(sub[i:], dots-1, new)
            return 
        
        solve(s, 3, "")
        return self.res


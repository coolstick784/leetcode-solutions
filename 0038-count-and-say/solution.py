class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"

        def getSay(s):
            print("s", s)
            fin = ""
            ctr = 1
            for idx, c in enumerate(s[1:]):

                if s[idx+1] != s[idx]:
                    fin += str(ctr)
                    fin += str(s[idx])
                    ctr = 1
                else:
                    ctr += 1
            fin += str(ctr)
            fin += str(s[-1])
            return fin
        for _ in range(n-1):
            s = getSay(s)
        return s
                        
            
        

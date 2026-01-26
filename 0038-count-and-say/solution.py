
class Solution:
    def countAndSay(self, n: int) -> str:
        i = 1
        target = n
        def returnSay(i, n):
            cur = ""
            n_str = str(n)
            idx = 0
            cur_d = n_str[0]
            cur_c = 0
            while idx < len(n_str):

                while idx < len(n_str) and n_str[idx] == cur_d :
                    cur_c += 1
                    idx += 1
                cur += str(cur_c)
                cur += str(cur_d)
                cur_c = 0
                if idx < len(n_str):
                    cur_d = n_str[idx]
            

            if i == 1:
                cur = "1"
            if i == target:
                return cur
            print("i", i)
            print("cur", cur)
            return returnSay(i+1, int(cur))
        return returnSay(i, n)

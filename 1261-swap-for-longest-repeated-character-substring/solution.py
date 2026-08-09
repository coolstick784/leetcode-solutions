class Solution:
    def maxRepOpt1(self, text: str) -> int:
        longest_swap = 0
        longest_no_swap = 0
        longest_swap_ch = None
        longest_swap_2 = 0
        longest_swap_2_ch = None
        longest_no_swap_ch = None
        res = 0
        ctr = Counter(text)
        for idx, ch in enumerate(text):
            print("idx", idx)
            print("longest swap", longest_swap, "longest swap ch", longest_swap_ch)
            print("lognest swap 2", longest_swap_2, "longtest swap 2 ch", longest_swap_2_ch)
            print("longest no swap", longest_no_swap, "longest no swap ch", longest_no_swap_ch)
            if idx == 0:
                longest_no_swap = 1
                longest_no_swap_ch = ch
                continue
            if ch != longest_swap_ch:
                longest_swap = 0
                longest_swap_ch = None
            else:
                longest_swap += 1
            if ch != longest_swap_2_ch:
                longest_swap_2 = 0
                longest_swap_2_ch = None
            else:
                longest_swap_2 += 1

            # if equal to previous, add 1 to longest no swap
            # if not equal to previous and equal to swap 2, add 
            if ch != longest_no_swap_ch:

                if ch == longest_swap_2_ch:
                    longest_swap_ch = longest_swap_2_ch
                    longest_swap = longest_swap_2
                longest_swap_2_ch = longest_no_swap_ch
                longest_swap_2 = longest_no_swap + 1

                longest_no_swap = 1
                longest_no_swap_ch = ch
            else:
                longest_no_swap += 1
            print("idx", idx, "longest swap", longest_swap, "longest no swap", longest_no_swap)
            
            res = max(res, min(longest_no_swap+1, len(text), ctr[longest_no_swap_ch]), min(ctr[longest_swap_ch], longest_swap), min(ctr[longest_swap_2_ch], longest_swap_2))
        return res

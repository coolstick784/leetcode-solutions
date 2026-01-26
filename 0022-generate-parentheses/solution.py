class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        cur_s = ""
        cur_stack = []
        final_len = n*2
        openings = ["(" for _ in range(n)]
        closings = [")" for _ in range(n)]
        def generateNext(cur, stack, cur_open, cur_close):

            if stack != []:
                print("adding close")
                generateNext(cur + ")", stack[:-1], cur_open, cur_close[:-1])
            if cur_open != []:

      
                generateNext(cur + "(", stack + ["("], cur_open[:-1], cur_close)
            if cur_open == [] and cur_close == []:

                out.append(cur)
        generateNext(cur_s, cur_stack, openings, closings)
        return out


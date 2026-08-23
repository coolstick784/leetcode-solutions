class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        ops = []
        nums = []
        cur = 0
        

        def do_op(op, n1, n2):
            if op == "*":
                return n1 * n2
            if op == "/":
                return n1 // n2
            if op == "+":
                return n1 + n2
            return n1 - n2
        for idx, ch in enumerate(s):
            if ch == "+" or ch == "-":
                if ops and ops[-1] in ["*", "/"]:
                    n1 = nums.pop()
                    n2 = cur
                    nums.append(do_op(ops.pop(), n1, n2))
                else:
                    nums.append(cur)

                ops.append(ch)
                cur = 0

            elif ch == "*":
                if ops and ops[-1] in ["*", "/"]:
                    n1 = nums.pop()
                    n2 = cur
                    nums.append(do_op(ops.pop(), n1, n2))
                else:
                    nums.append(cur)
                ops.append(ch)
                
                cur = 0
            elif ch == "/":
                if ops and ops[-1] in ["*", "/"]:
                    n1 = nums.pop()
                    n2 = cur
                    nums.append(do_op(ops.pop(), n1, n2))
                else:
                    nums.append(cur)
                ops.append(ch)
                
                cur = 0


            
            else:
                cur = 10 * cur + int(ch)
        if ops and ops[-1] in ["*", "/"]:
            n1 = nums.pop()
            n2 = cur
            nums.append(do_op(ops.pop(), n1, n2))
        else:
            nums.append(cur)
        res = nums[0]
        for idx, n in enumerate(nums[1:]):
            op = ops[idx]
            res = do_op(op, res, n)
        return res

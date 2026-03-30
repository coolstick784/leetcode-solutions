class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        # We want a list of populated values and the index we are currently at for each of the left and right
        # Each populated value should either correspond to 2 indices or 0
        # The LR dict should have the index of the root, and its left/right indices
        # If the root is null, or a populated value only has 1 left/right, return false
        l_stack = []
        r_stack = []
        chs = preorder.split(",")
        if len(chs) == 1 and chs[0] != '#':
            return False
        for idx, ch in enumerate(chs):
            
            if idx == 0:
                pass
            elif l_stack != []:
                l_stack.pop()
            elif r_stack != []:
                r_stack.pop()
            else:
                return False
            if ch != "#":
                l_stack.append(ch)
                r_stack.append(ch)


            print("idx", idx)
            print("ch", ch)
            print("l stack", l_stack)
            print("r stack", r_stack)
        if len(l_stack) == len(r_stack):
            return True
        return False
            




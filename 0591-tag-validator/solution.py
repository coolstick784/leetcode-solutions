class Solution:
    def isValid(self, code: str) -> bool:

        upper = set()
        for n in range(26):
            upper.add(chr(ord('A') + n))
        
        
        def valid():
            if len(code) < 3:
                print("len bad")
                return False
            if not code[0] == "<" and code[-1] == ">":
                print("s/e not valid")
                return False
            tag = []
            idx = 1
            
            while idx < len(code) and code[idx] != ">":
                ch = code[idx]
                tag.append(ch)
                idx += 1
                
                if ch not in upper:
                    print("not upper")
                    return False
            if len(tag) < 1 or len(tag) > 9:
                print("len bad")
                return False
            
            idx = len(code) - 2
            
            while idx >= 0 and code[idx-1:idx+1] != "</":
                if not tag:
                    print("no tag p2")
                    return False
                ch = code[idx]
                if ch != tag.pop():
                    print("not equal p2")
                    return False

                idx -= 1
            return True
            
                
        if not valid():
            print("not valid")
            return False

        stack = []
        cur = []
        cdata = False
        start_tag = False
        end_tag = False
        tag_content = True
        idx = 0
        while idx < len(code):
            ch = code[idx]
            print("Idx", idx, "ch", ch, "tag content", tag_content)
            
            if cdata and idx < len(code) - 2 and code[idx:idx+3] == "]]>":
                idx += 3
                cdata = False
                tag_content = True
                
            elif start_tag and ch == ">":
                cur_tag = "".join(cur)
                
                cur = []
                if len(cur_tag) < 1 or len(cur_tag) > 9:
                    print("len bad")
                    return False
                stack.append(cur_tag)
                start_tag = False
                tag_content = True
                idx += 1
                
            elif end_tag and ch == ">":
                cur_tag = "".join(cur)
                cur = []
                end_tag = False
                if not stack or cur_tag != stack.pop():
                    print("not equal")
                    return False
                tag_content = True
                idx += 1
            elif tag_content and idx < len(code) - 9 and code[idx:idx+9] == r"<![CDATA[":
                idx += 8
                cdata = True
                tag_content = False
            elif tag_content and idx < len(code) - 1 and code[idx:idx+2] == r"</":
                idx += 2
                cur = []
                end_tag = True
                tag_content = False
            elif tag_content and code[idx] == "<":
                idx += 1
                cur = []
                start_tag = True
                tag_content = False
            elif cdata:
                idx += 1
            elif start_tag or end_tag:
                if ch not in upper:
                    print("not upper")
                    return False
                cur.append(ch)
                idx += 1
            else:
                idx += 1
        
        if stack or end_tag or start_tag or cdata or not tag_content:
            print("one of end")
            return False
        return True

            
            



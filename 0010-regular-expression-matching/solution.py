class Solution:
    
    def isMatch(self, s: str, p: str) -> bool:
        match_idx = 0
        match = s
        found_match = False
        foo = list(p)
        ctr = 0
        
        for idx, char in enumerate(p):
            
            if len(p) > (idx+3) and p[idx+2] == char and p[idx+3] == "*" and p[idx+1] == "*":
                print("1", foo[idx - ctr*2])
                print("2",foo[idx+1 - ctr*2] )
                del foo[idx - ctr*2]
                del foo[idx - ctr*2]
                ctr += 1
        p = "".join(foo)
        
        just_removed = ""
        for idx, char in enumerate(p):

            if char == "*":
                continue


            if char == ".":
                
                if idx < len(p) - 1 and p[idx + 1] == "*":
                    just_removed_bool = False
                    if p[idx:] == ".*":
                        return True
                    else:
                        t_idx = len(match) - 1
                        
                        for c_idx in range(t_idx, -1, -1):

                            
                            if self.isMatch(match[c_idx:], p[idx+2:]) :
                               
                                match_idx += c_idx
                                found_match = True

                                #print("is match", self.isMatch("caa", "c*.c*.a*c"))
                                break
                            elif self.isMatch("", p[idx+2:]):
                               
                                match_idx += c_idx+1
                                found_match = True

                                break
                        if found_match == False:
                            return False
                elif match != "":
                    just_removed_bool = False
                    match_idx += 1
                elif just_removed != "" and (
                    (p[idx - 1] and p[idx - 1] == "*") or just_removed_bool == True
                ):
                    if just_removed[0]:
                        just_removed = just_removed[1:]
                   
                        just_removed_bool = True

                    else:
                        return False
                else:
                    return False

            elif idx < len(p) - 1 and p[idx + 1] == "*":

                t_idx = 0
                for match_char in match:
                    if match_char == char:
                        t_idx += 1
                    else:
                        break
                for c_idx in range(t_idx, -1, -1):


                    if self.isMatch(match[c_idx:], p[idx+2:]) :

                        match_idx += c_idx
                        found_match = True

                        #print("is match", self.isMatch("caa", "c*.c*.a*c"))
                        break

                if found_match == False:
                    return False

            else:


                if len(match) > 0 and match[0] == char:
                    just_removed_bool = False
                    match_idx += 1
                elif just_removed != "" and (
                    (p[idx - 1] and p[idx - 1] == "*") or just_removed_bool == True
                ):
                    if just_removed[0] == char:
                        just_removed = just_removed[1:]

                        just_removed_bool = True
                    elif len(match) > 0 and match[0] == char:
                        just_removed_bool = False
                        match_idx += 1
                    else:
                        return False

                else:
                    return False
            match = s[match_idx:]

        if match == "":
            return True
        else:
            return False



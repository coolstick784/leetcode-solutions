# have our res be a list we can join later on so we're not creating a new string every time
# first, create an indices dictionary where we have the index, source, target, and also the corresponding characters from s
# loop through each source idx in a while loop
# if it's not in indices, add it to res
# if it's in indices but there's no match, add it to res
# if it's in indices and there is a match, add the target to res and move forward len(current source) chars 

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        res = []
        
        indices_dict = {}
        for idx, i in enumerate(indices):
            indices_dict.setdefault(i, []).append(
                {
                    "source":sources[idx],
                    "target":targets[idx],
                    "corr":s[i:i+len(sources[idx])]
                }
            )
        
        s_idx = 0
        while s_idx < len(s):

            cur_s = s[s_idx]
            if s_idx not in indices_dict:
                res.append(cur_s)
                s_idx += 1
            elif s_idx in indices_dict:
                found = False
                for cur_dict in indices_dict[s_idx]:

                    if cur_dict["source"] == cur_dict["corr"]:
                        res.append(cur_dict["target"])
                        s_idx += len(cur_dict["source"])
                        found = True
                if not found:
                    res.append(cur_s)
                    s_idx += 1




        return "".join(res)
        

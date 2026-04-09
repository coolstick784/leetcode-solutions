# 1. add each name to all names if it doesnt exist in all_names and add it to res
# 2. set the mapping dict of that name to 0
# 3. if it is in all_names:
# add 1 to map_dict (which was previously k-1), and check if adding (k) is in all_names
# if it is, continue the process until it isn't
# then, add it to all_names, add it to map_dict with value 0, and add it to res

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        res = []
        map_dict = {}
        all_names = set()
        for name in names:
            if name not in all_names:
                all_names.add(name)
                map_dict[name] = 0
                res.append(name)
                continue
            if name in all_names:
                map_dict[name] += 1
                cur_name = name + "(" + str(map_dict[name]) + ")"
                while cur_name in all_names:
                    map_dict[name] += 1
                    cur_name = name + "(" + str(map_dict[name]) + ")"
                all_names.add(cur_name)
                map_dict[cur_name] = 0
                res.append(cur_name)
        return res


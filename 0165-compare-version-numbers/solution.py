class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(s) for s in version1.split(".")]
        v2 = [int(s) for s in version2.split(".")]
        max_l = max(len(v1), len(v2))
        for idx in range(max_l):
            if idx < len(v1):
                cur_v1 = v1[idx]
            else:
                cur_v1 = 0
            if idx < len(v2):
                cur_v2 = v2[idx] 
            else:
                cur_v2 = 0
            if cur_v1 > cur_v2:
                return 1
            elif cur_v2 > cur_v1:
                return -1
        return 0

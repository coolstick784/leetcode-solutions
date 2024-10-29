class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        my_dict = {}

        for s in strs:
            cur_sorted = ''.join(sorted(s))
            try:
                my_dict[cur_sorted].append(s)
            except:
                my_dict[cur_sorted] = [s]
        return list(my_dict.values())

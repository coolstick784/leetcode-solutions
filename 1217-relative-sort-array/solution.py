# have a new array with a tuple
# the first el will be the index in arr2, the second will be the num
# if it's not in arr2, set it to 2k
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        new = []
        idx_dict = {}
        for idx, el in enumerate(arr2):
            idx_dict[el] = idx
        for n in arr1:
            new.append((idx_dict.get(n, 2000), n))
        new.sort()
        return [n[1] for n in new]

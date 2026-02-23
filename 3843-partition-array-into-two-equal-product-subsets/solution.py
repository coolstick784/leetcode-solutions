class Solution:
    

    def findSubset(self, target, cur_list, idxs, nums):

        if cur_list == []:
            return
        if target == 1:
            self.subset= idxs
        if cur_list[0] == target:

            self.subset = idxs + [nums.index(cur_list[0])]

     
        if cur_list[0] < target and target % cur_list[0] == 0:
            self.findSubset(target/cur_list[0], cur_list[1:], idxs + [nums.index(cur_list[0])], nums)

        self.findSubset(target, cur_list[1:], idxs, nums)
    
    
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        


        self.subset = []
        self.findSubset(target/nums[0], nums[1:], [0], nums)

        mul = 1
        for idx, n in enumerate(nums):
            if idx not in self.subset:
                mul *= n
        if mul == target:
            return True
        return False


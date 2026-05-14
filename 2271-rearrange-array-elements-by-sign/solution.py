class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = deque([])
        negatives = deque([])
        out = []
        need = "pos"
        for n in nums:
            if n > 0:
                positives.append(n)
            else:
                negatives.append(n)

        while positives and negatives:
            out.append(positives.popleft())
            out.append(negatives.popleft())
        return out

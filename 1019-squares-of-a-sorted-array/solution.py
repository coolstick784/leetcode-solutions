class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_squares = [n*n for n in nums if n < 0]
        pos_squares = [n*n for n in nums if n >= 0]
        res = []
        neg_squares.reverse()
        neg_left =0 
        pos_left = 0
        ctr  = 0
        
        # If we've went through all the positives, or the negative is less, add the negative
        # Otherwise, add the positive
        while ctr < len(nums):
            if neg_left < len(neg_squares) and (pos_left >= len(pos_squares) or neg_squares[neg_left] < pos_squares[pos_left]):
                res.append(neg_squares[neg_left])
                neg_left += 1
            else:
                res.append(pos_squares[pos_left])
                pos_left += 1
        
            ctr += 1
        return res

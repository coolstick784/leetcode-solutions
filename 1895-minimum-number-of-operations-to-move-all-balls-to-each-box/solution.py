class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        left_sum = 0
        left_n = 0
        right_sum = 0
        right_n = 0
        for idx in range(len(boxes)-1, -1, -1):
            ch = boxes[idx]
            if ch == '1':
                right_n += 1
                right_sum += idx
        
        prev = 0
        res = []
        for idx, ch in enumerate(boxes):
            
            if ch == '1':
                prev = 1
                right_n -= 1
            else:
                prev = 0

            res.append(left_sum + right_sum)
            left_n += prev
            left_sum += left_n
            right_sum -= right_n
        return res
            

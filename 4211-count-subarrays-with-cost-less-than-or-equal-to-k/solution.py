class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        min_heap = [(nums[0], 0)] # (n, idx)
        max_heap = [(-nums[0], 0)] # (-n, idx)
        res = 0

        def isValid(mn, mx, cur, dist, k):
            #print(mn, mx, cur, dist, k)
            if (max(mx, cur) - min(mn, cur)) * dist <= k:
                return True
            return False

        while left < len(nums):
            right = max(left, right)
            while min_heap and min_heap[0][1] < left:
                heapq.heappop(min_heap)
            while max_heap and max_heap[0][1] < left:
                heapq.heappop(max_heap)
            if not min_heap:
                heapq.heappush(min_heap, (n, left))
                heapq.heappush(max_heap, (-n, left))
            to_break = False
            while right < len(nums)-1 and not to_break :
                
                right += 1
                n = nums[right]

                if isValid(min_heap[0][0], -max_heap[0][0], n, right-left+1, k):
                    heapq.heappush(min_heap, (n, right))
                    heapq.heappush(max_heap, (-n, right))
                else:
                    right -= 1
                    to_break = True
            #print("left", left, "rgiht", right)
            res += right - left + 1
            left += 1
        return res
                

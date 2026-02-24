class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        # Find the longest non decreasing starting from the left
        # Find the longest non decreasing ending at the right
        # Figure out if you want to drop the rightmost from the start or the leftmost from the end
        # Continue the process until the joining is non decreasing

        # To figure out which to drop, we can get the number of values in the left less than each x from 1 to x
        # similarly, the # of values in the right less than y from 1 to y

        left_start = 0
        left_end = 0
        while left_end < len(arr) -1  and arr[left_end + 1] >= arr[left_end]:
            left_end += 1
        if left_end == len(arr) - 1:
            return 0
        right_start = len(arr)- 1
        right_end = len(arr) - 1
        while right_start > 0 and arr[right_start - 1] <= arr[right_start]:
            right_start -= 1

        l = arr[left_end]
        right = right_start
        num_more = 0
        while right < len(arr) and l > arr[right] :
            right += 1
            num_more += 1
        right -= 1
        r = arr[right_start]
        left = left_end
        num_less = 0
        while left >= 0 and r < arr[left]:
            left -= 1
            num_less += 1
        left += 1
        
        print("left end", l)
        print("right start", r)
        print("num more", num_more)
        print("num less", num_less)
        print("\n\n")
        while arr[left_end] > arr[right_start]:
            
            
            if num_less < num_more:
                if arr[left_end] > arr[right_start]:
                    num_less -= 1
                left_end -= 1
                if left_end == -1:
                    return len(arr) - (right_end - right_start) - 1
                while right >= 0 and arr[left_end] <= arr[right]:
                    right -= 1
                    num_more -= 1
                

            else:
                if arr[right_start] < arr[left_end]:
                    num_more -= 1
                right_start += 1
                if right_start == len(arr):
                    return len(arr) - (left_end - left_start) - 1

                print("right start", arr[right_start])
                print("prev num less", num_less)
                print("left", left)

                while left < len(arr) and arr[right_start] >= arr[left]:
                    left += 1
                    num_less -= 1
                print("after num less", num_less)
                
            print("right start", arr[right_start])
            print("num more", num_more)
            print("left end", arr[left_end])
            print("num less", num_less)

            print("\n")
        print("right start", right_start)
        print("left end", left_end)
        print("right end", right_end)
        print("left start", left_start)
        return len(arr) - (right_end -right_start + 1) - (left_end - left_start + 1)
            



        

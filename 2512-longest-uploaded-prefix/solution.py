# when we upload a video, we first set its index in the arr to True
# then, if it's the longest prefix + 1, we add 1 to the longest while the next has been uploaded

class LUPrefix:

    def __init__(self, n: int):
        self.longest_val = 0
        self.arr = [False for _  in range(n)]
        

    def upload(self, video: int) -> None:
        self.arr[video-1] = True
        if video == self.longest_val + 1:
            cur = video-1
            while cur < len(self.arr) and self.arr[cur] == True:
                self.longest_val += 1
                cur += 1
        

    def longest(self) -> int:
        return self.longest_val


# [False, False, False, False] 0 
# [False, False, True, False] 0
#[True, False, True, False] 1
# [True, True, True, False]
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()

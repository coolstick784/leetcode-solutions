class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.dn = "East"
        self.r = 0
        self.c = 0
        self.loop_dist = self.w + self.w + self.h + self.h - 4
        print("loop dist", self.loop_dist)
        self.dns = ["East", "North", "West", "South"]
    
    def changeDn(self):

        idx = self.dns.index(self.dn)
        self.dn = self.dns[(idx+1) % 4]


        

    def step(self, num: int) -> None:
        
        n = num
        while n > 0:
            invalid = True
            if self.c == self.w - 1 or self.r == self.h - 1 or self.c == 0 or self.r == 0:
                if n > self.loop_dist:
                    if self.c == 0 and self.r == 0:
                        self.dn = "South"
                    elif self.c == self.w-1 and self.r == 0:
                        self.dn = "East"
                    elif self.c == self.w-1 and self.r == self.h - 1:
                        self.dn = "North"
                    elif self.c == 0 and self.r == self.h-1:
                        self.dn = "West"
                n = n % self.loop_dist

                if n == 0:
                    break
            while invalid:
                if self.dn == "East" and self.c+1 < self.w:
                    self.c += 1
                    invalid = False
                elif self.dn == "North" and self.r + 1 < self.h:
                    self.r += 1
                    invalid = False
                elif self.dn == "West" and self.c-1 >= 0:
                    self.c -= 1
                    invalid = False
                elif self.dn == "South" and self.r-1 >= 0:
                    self.r -= 1
                    invalid = False
                else:
                    self.changeDn()
            n -= 1

    def getPos(self) -> List[int]:
        return [self.c,self.r]
        

    def getDir(self) -> str:
        return self.dn
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()

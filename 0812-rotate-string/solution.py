class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s += s
        
        for start in range(len(goal)):
            cur = s[start:start+len(goal)]
            if cur == goal:
                return True
        return False
        

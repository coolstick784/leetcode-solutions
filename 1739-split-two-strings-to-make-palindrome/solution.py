# we have 3 things to take into account
# we have to take the start from A into account, the end from B, and the start from B]
# once the start from A stops being a palindrome, take over from the corr index on B
# do the reverse with B start, A end

class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        

        start_idx = 0
        end_idx = len(a) - 1

        def isPalindrome(s):
            out = True
            start = 0
            end = len(s) - 1
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1 

            return True
        while start_idx < end_idx and a[start_idx] == b[end_idx]:
            start_idx += 1
            end_idx -= 1
        if start_idx >= end_idx or isPalindrome(a[start_idx:end_idx+1]) or isPalindrome(b[start_idx:end_idx+1]):
            return True

        start_idx = 0
        end_idx = len(a) - 1

        while start_idx < end_idx and b[start_idx] == a[end_idx]:
            start_idx += 1
            end_idx -= 1
        if start_idx >= end_idx or isPalindrome(a[start_idx:end_idx+1]) or isPalindrome(b[start_idx:end_idx+1]):
            return True

        return False    
        

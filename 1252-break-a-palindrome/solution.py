# replace the first non a with an A
# this would break if:
# the a is the middle position and the length of the palindrome is odd. if this is the case, replace the one to the left with b. if len(palindrome) == 1, return ""
# if it is all A's, switch the last one with a b
# if it's all A's except for the middle, replace the last one with a b
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        if list(set(palindrome)) == ['a']:
            return palindrome[:-1] + 'b'

        if len(palindrome) % 2 == 1:
            middle = len(palindrome) // 2
            without_middle = palindrome[:middle] + palindrome[middle+1:]
            
            if list(set(without_middle)) == ['a']:
                return palindrome[:-1] + 'b'
        for idx, ch in enumerate(palindrome):
            if ch != 'a':
                return palindrome[:idx] + 'a' + palindrome[idx+1:]
        

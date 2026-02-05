class Solution(object):
    def reportSpam(self, message, bannedWords):
        keys = set(bannedWords)
        return sum(1 for word in message if word in keys) > 1  

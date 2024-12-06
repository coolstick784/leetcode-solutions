class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        self.final = []
        self.start = False
        for word in words:
            if len(word) == 1:
                self.nextWord(word, words)   
                self.start = True
        if not self.start:
            return ""
        
        self.max = max([len(word) for word in self.final])
        self.res = min([word for word in self.final if len(word) == self.max])
        return self.res
    def nextWord(self, word, words):
        found = False
        for nextWord in words:
            if len(nextWord) == len(word) + 1 and nextWord[:len(word)] == word:
                found = True
                self.nextWord(nextWord, words)
        if found == False:
            self.final.append(word)
        
        

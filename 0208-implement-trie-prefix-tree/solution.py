# dict of dicts
# if we add something, e.g. add {k:{e:{y: True:<full word>}}}


# {a:{}}
# {a:{p:{True:ap}}}

class Trie:

    def __init__(self):
        self.dicts = {}
        

    def insert(self, word: str) -> None:
        prev = self.dicts
        for idx, ch in enumerate(word):
            prev.setdefault(ch, {})
            if idx == len(word) - 1:
                prev[ch][True] = word
            prev = prev[ch]

    def search(self, word: str) -> bool:
        prev = self.dicts
        for ch in word:
            prev = prev.get(ch, {})
        if True in prev:
            return True
        return False 

        

    def startsWith(self, prefix: str) -> bool:
        prev = self.dicts
        for ch in prefix:
            prev = prev.get(ch, {})
        if prev != {}:
            return True
        return False    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

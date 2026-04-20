# WE CAN kinda flip it, asking, for each vowel, how many substrings is it a part of?

# 1. all the substrings that start at that number or to the left of it, so that number of chars, * the number of chars that end at that index or to the right of it

class Solution:
    def countVowels(self, word: str) -> int:
        ctr = 0
        vowels = set(["a", "e", "i", "o", "u"])
        for idx, ch in enumerate(word):
            if ch in vowels:
                ctr += (idx+1) * (len(word)-idx)
        return ctr

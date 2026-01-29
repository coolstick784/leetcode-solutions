class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        correct = 0
        num_floating = {}
        for idx, s in enumerate(secret):
            if s == guess[idx]:
                correct += 1
            else:
                num_floating[s] = 1 + num_floating.get(s, 0)
        res = str(correct) + "A"
        B = 0
        for idx, ch in enumerate(guess):
            if num_floating.get(ch, 0) > 0 and ch != secret[idx]:
                num_floating[ch] -= 1
                B += 1
        res += str(B) + "B"
        return res



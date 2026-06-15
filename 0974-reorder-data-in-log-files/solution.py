class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        ds = [str(n) for n in range(10)]
        for log in logs:
            cleaned = log.lstrip(" ")
            val =  cleaned.split(" ")[1:]
            isDigit = False
            for d in ds:
                if d in "".join(val):
                    
                    digits.append(log)
                    isDigit = True
                    break
            if not isDigit:
                letters.append(log)
        letters = [(" ".join(log.split(" ")[1:]), log.split(" ")[0]) for log in letters]
        letters.sort()
        
        new = []
        for c, i in letters:

            new.append(i + " " + c)
        print(digits)
        
        return new + digits

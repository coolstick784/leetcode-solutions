class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        discount = float(discount)
        digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        words = sentence.split()
        updated = []
        for word in words:
            if word[0] == "$" and len(word) > 1:
                is_n = True
                number_str = ""
                for ch in word[1:]:
                    if ch in digits:
                        number_str += ch
                    else:
                        is_n = False
                if not is_n:
                    updated.append(word)
                else:
                    cur = "$"
                    n = round(float(int(number_str)) * (1-discount / 100.0), 2)
                    str_n = str(n)
               
                    if len(str_n.split(".")[1]) == 1:
                        str_n += "0"
                    cur += str_n
                    updated.append(cur)
            else:
                updated.append(word)
        return (" ").join(updated)

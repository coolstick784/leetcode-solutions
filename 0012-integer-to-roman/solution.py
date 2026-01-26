class Solution:
    def intToRoman(self, num: int) -> str:
        cur = num
        fin = ""
        while cur > 0:
            as_s = str(cur)
            first = int(as_s[0])
            len_n = len(as_s)
            print("as s", as_s)
            print("first", first)

            if len_n == 4:
                for _ in range(first):
                    fin += "M"
                    cur -= 1000 
            elif len_n == 3:
                if first == 4:
                    fin += "CD"
                    cur -= 400
                elif first == 9:
                    fin += "CM"
                    cur -= 900

                elif first >= 5:
                        cur -= 500
                        fin += "D"
                else:
                    for _ in range(first):
                        fin += "C"
                        cur -= 100 
            elif len_n == 2:
                if first == 4:
                    fin += "XL"
                    cur -= 40
                elif first == 9:
                    fin += "XC"
                    cur -= 90
                elif first >= 5:
                    fin += "L"
                    cur -= 50
                else:
                    for _ in range(first):
                        fin += "X"
                        cur -= 10
            else:
                if first == 4:
                    fin += "IV"
                    cur -= 4
                elif first == 9:
                    fin += "IX"
                    cur -= 9
                elif first >= 5:
                    fin += "V"
                    cur -= 5
                else:
                    for _ in range(first):
                        fin += "I"
                        cur -= first
            print('cur', cur)
        return fin

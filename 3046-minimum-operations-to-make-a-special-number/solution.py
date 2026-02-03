class Solution:
    def minimumOperations(self, num: str) -> int:
        # Find the rightmost 0 -> 0, 5 ->0 , 2-> 5, or 7 -> 5, then find the number of digits between the last and first, and subtract 1 from that
        # If there isn't a match, but there is a 0 or 5, return the number of digits - 1
        # If there no match, return the number of digits



        def first50(num):
            ctr = 0
            for idx, ch in enumerate(num[::-1]):


                if ctr >= 1 and (ch == "0" or ch == "5"):

                    return idx + 1 - 2
                if ch == "0":
                    ctr += 1
            if ctr == 1:
                return len(num) - 1
            return 2**31-1
        def first25(num):
            ctr = 0
            for idx, ch in enumerate(num[::-1]):
                if ch == "5":
                    ctr += 1
                elif ctr >= 1 and (ch == "2" or ch == "7"):
                    return idx + 1 - 2

            return 2**31-1
        print("first 50", first50(num))
        return min([len(num), first50(num), first25(num)])


        

        

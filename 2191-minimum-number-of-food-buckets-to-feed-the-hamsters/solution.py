class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        # We can start from the left
        # If the first hamster has another hamster after skipping one, place a food bucket between the hamsters. 
        # Otherwise, place a food bucket to the left/right, whichever is feasible
        # After a hamster is fed, we start on the next one and it can basically be ignored

        left = 0
        res = 0
        while left < len(hamsters):
            cur = hamsters[left]
            if cur != "H":
                left += 1
            else:
                if left < len(hamsters) - 2 and hamsters[left+2] == "H" and hamsters[left+1] == ".":
                    res += 1
                    left += 3
                elif left >= 1 and hamsters[left-1] == ".":
                    res += 1
                    left += 1
                elif left < len(hamsters) - 1 and hamsters[left+1] == ".":
                    res += 1
                    left += 2
                else:
                    return -1

        return res

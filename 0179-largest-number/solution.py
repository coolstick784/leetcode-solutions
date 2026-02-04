from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # 1) convert to strings
        store = [str(num) for num in nums]

        # 2) comparator: decide order of two strings a and b
        def compare(a: str, b: str) -> int:
            # if putting a before b makes a bigger combined number, a should come first
            if a + b > b + a:
                return -1   # a comes before b
            elif a + b < b + a:
                return 1    # b comes before a
            else:
                return 0    # either order is fine

        # 3) sort using the comparator
        store.sort(key=cmp_to_key(compare))

        # 4) handle all zeros
        if store[0] == "0":
            return "0"

        # 5) join into the final answer
        return "".join(store)


class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        max_val = max(groups)

        # ans[x] = smallest index of an element that divides x
        ans = [-1] * (max_val + 1)

        seen = set()

        # go in original index order, so the first valid index is automatically the smallest
        for idx, el in enumerate(elements):
            if el in seen:
                continue
            seen.add(el)

            if el > max_val:
                continue

            for multiple in range(el, max_val + 1, el):
                if ans[multiple] == -1:
                    ans[multiple] = idx

        return [ans[g] for g in groups]

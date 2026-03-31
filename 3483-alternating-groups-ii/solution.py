class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res = 0

        # At each index, we want the longest alternating sequence ending at that index
        # If it's >= k, add it
        arr = [1 for _ in range(len(colors))]
        
        for idx, c in enumerate(colors):
            if c != colors[idx-1]:
                arr[idx] = arr[idx-1] + 1

        if colors[-1] != colors[0]:
            for idx, c in enumerate(colors[:k]):
                if arr[idx] != 1:
                    arr[idx] = arr[-1] + arr[idx] - 1
                else:
                    break
        print("arr", arr)



        for n in arr:
            if n >= k:
                res += 1
        return res

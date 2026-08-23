class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        arr = [0 for _ in range(n)]
        ans = []
        res = 0
        for idx, (i, color) in enumerate(queries):

            if ((i < len(arr) - 1) and arr[i] == arr[i+1] and arr[i] != 0):
                res -= 1
            if i > 0 and arr[i] == arr[i-1] and arr[i] != 0:
                res -= 1
            arr[i] = color
            if ((i < len(arr) - 1) and arr[i] == arr[i+1] and arr[i] != 0):
                res += 1
            if i > 0 and arr[i] == arr[i-1] and arr[i] != 0:
                res += 1
            ans.append(res)
            #print("arr", arr, "res", res)
        return ans


class Solution:
    def arrangeWords(self, text: str) -> str:
        heap = []
        for idx, word in enumerate(text.split()):
            heapq.heappush(heap, (len(word), idx, word))
        res = []
        while heap:
            res.append(heapq.heappop(heap)[2].lower())


        res = " ".join(res)
        res = res[0].upper() + res[1:]
        return res

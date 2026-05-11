class Solution:
    def reorganizeString(self, s: str) -> str:
        ctr = Counter(s)
        heap = []
        for ch in ctr:
            heapq.heappush(heap, (-ctr[ch], ch))
        cur_ch = ""
        res = ""
        while heap:
            val, ch = heapq.heappop(heap)
            if ch == cur_ch and heap:
                next_val, next_ch = heapq.heappop(heap)
                res += next_ch
                cur_ch = next_ch
                next_val += 1
                if next_val < 0:
                    heapq.heappush(heap, (next_val, next_ch))
                heapq.heappush(heap, (val, ch))
            elif ch != cur_ch:
                val += 1
                res += ch
                if val < 0:
                    heapq.heappush(heap, (val, ch))
                cur_ch = ch
        if len(res) < len(s) :
            return ""



        return res



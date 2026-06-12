class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        idxs = Counter(s)
        letters = [chr(ord('a') + n) for n in range(26)]
        # what's the smallest letter such that everything else fits to the right of it

        def solve(start, ctr):
            heap = []
            new = ctr.copy()
            left = start

            if not new:
                return []
            while True:

                ch = s[left]
                if ch not in new:
                    left += 1
                    continue
                heapq.heappush(heap, (ch, left))
                new[ch] -= 1
                if new[ch] == 0:
                    remove, new_start = heapq.heappop(heap)


                    for right in range(left, new_start, -1):
                        if s[right] in new:
                            new[s[right]] += 1
          
                    del new[remove]

            
                    return [remove] + solve(new_start+1, new)


                left += 1



        return "".join(solve(0, idxs))

        

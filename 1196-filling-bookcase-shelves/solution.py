# for each book, we can either add it to the current shelf or create a new shelf
# therefore, we want the index of the current book, the height of the shelf up to that point, and the remaining width of the current shelf as arguments
# we wanttheminuimum of either creating a new shelf or adding to the current

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache(None)
        def solve(idx, cur_h, rem_w):
            if idx >= len(books):
                return cur_h
            out = []
            thick, h = books[idx]
            if rem_w >= thick:
                out.append(solve(idx+1, max(cur_h, h), rem_w-thick))
            out.append(cur_h + solve(idx+1, h, shelfWidth-thick))


            return min(out)
        

        return solve(0, 0, shelfWidth)
        

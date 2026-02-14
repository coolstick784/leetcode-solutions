class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_a = None
        fruit_b = None
        fruit_a_start = -1
        fruit_b_start = -1
        last_fruit_a = -1
        last_fruit_b = -1
        max_len = 0
        recent = None
        for idx, f in enumerate(fruits):

            
            if f != fruit_a and f != fruit_b:
                if recent == fruit_a:
                    fruit_a_start = last_fruit_b + 1
                    fruit_b_start = idx
                    fruit_b = f

                else:
                    fruit_b_start = last_fruit_a + 1
                    fruit_a_start = idx
                    fruit_a = f

            if f == fruit_a:
                last_fruit_a = idx
            else:
                last_fruit_b = idx
            recent = f
            cur_len = idx - max(min(fruit_a_start, fruit_b_start), 0) + 1

            max_len = max(max_len, cur_len)
        
        
        
        return max_len
        

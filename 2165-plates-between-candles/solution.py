# we want to know the index of the candle furthest right in the substr, the index of the candle furthest to the left, and the number of candles in between
# then, our answer is right - left - num candles in between
# we can have an array with the candle closest to the index from the left as well as to the right
# we'll default at -1 so we know if it's null
# starting from the left, if there is a candle at that idx, that idx is our value, otherwise it's the value of our previous idx
# if the idx is 0, then there either is a candle or it's -1
# and this will tell us the candle closest to the end of the substring ending at idx
# same with looping from the right the other way around
# to get number of candles, we just add a number to the previous if there is a candle there
# num candles = num at end - num at start - 1
# num candles represents before



# s = "**|**|***|", queries = [[2,5],[5,9]]

# furthest_right = [0, 0, 2, 2, 2, 5, 5, 5, 5, 9]
# furthest_left = [2, 2, 2, 5, 5, 5, 9, 9, 9, 9]
# num_candles = [0, 0, 0, 1, 1, 1, 2, 2, 2, 2]

# [2, 5]
#r = 5, l = 2, num_candles[end] - num_candles[start] + add -2 =0 2
# 
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        furthest_right = [-1 for _ in range(len(s))]
        furthest_left = [-1 for _ in range(len(s))]
        num_candles = []
        for idx in range(len(s)):
            if idx == 0 and s[0] == "|":
                furthest_right[0] = 0
            elif idx != 0:
                if s[idx] == "|":
                    furthest_right[idx] = idx
                else:
                    furthest_right[idx] = furthest_right[idx-1]
        for idx in range(len(s)-1, -1, -1):
            if idx == len(s)-1 and s[idx] == "|":
                furthest_left[idx] = idx
            elif idx != len(s) - 1:
                if s[idx] == "|":
                    furthest_left[idx] = idx
                else:
                    furthest_left[idx] = furthest_left[idx+1]
        cur = 0
        for idx, ch in enumerate(s):

            num_candles.append(cur)
            if ch == "|":
                cur += 1
        
        res = []
        for start, end in queries:
            add = 0
            if s[end] == "|":
                add = 1
            if furthest_right[end] ==-1 or furthest_left[start] == -1:
                res.append(0)
            elif furthest_right[end] > furthest_left[start]:
                res.append(furthest_right[end] - furthest_left[start] -1 - (num_candles[end] - num_candles[start] + add -2))
            
            else:
                res.append(0)
        return res

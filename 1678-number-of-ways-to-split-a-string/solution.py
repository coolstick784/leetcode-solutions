class Solution:
    def numWays(self, s: str) -> int:
        # 1. Count the number of 1's
        # 2. Divide that by 3. If it's not divisible by 3, return 0
        # 3. Get the index of the last 1 from the first group, the first 1 from the second group, the last 1 from the second group, and the first 1 from the 3rd group
        # 4. If the difference between the last 1 from the first group and first 1 from 2nd is n1, then we have n1 possibilites for that line
        # Similarly, we have (first from 3rd - last from 2nd) = n2 possibilites for the 2nd line
        # Our answer is then n1 * n2

        ctr = Counter(s)
        if ctr["1"] % 3 != 0:
            return 0
        num_each = ctr["1"] // 3
        landmark = [None, None, None, None] # 2nd from 1st, 1st from 2nd, 2nd from 2nd, 1st from 3rd
        cur_ctr = 0
        landmark_num = 0
        print("num each", num_each)
        for idx, ch in enumerate(s):
            if ch == "1":

                cur_ctr += 1
                if cur_ctr == num_each and landmark_num ==  0:
                    landmark[landmark_num] = idx
                    landmark_num += 1
                    
                elif landmark_num == 1:
                    landmark[landmark_num] = idx
                    landmark_num = 2
                    if num_each == 1:
                        landmark[2] = idx
                        landmark_num = 3
                elif landmark_num == 2 and cur_ctr == num_each * 2:
                    landmark[landmark_num] = idx
                    landmark_num = 3
                elif landmark_num ==3:
                    landmark[landmark_num] = idx
                    landmark_num = 4
        if ctr["1"] == 0:
            # if left after 1st 0 and n=4, can have 2
            # if left after 2nd 0 and n=4, can have 1
            res = 0
            for n in range(len(s) -2, 0, -1):
                res += n
            return res % (10**9 + 7)
        print("landmarks", landmark)
        return (landmark[1] - landmark[0]) * (landmark[3] - landmark[2]) % (10**9 + 7)


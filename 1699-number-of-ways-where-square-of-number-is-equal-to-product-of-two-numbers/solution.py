class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:

        ctr1 = Counter(nums1)
        nums1 =set(nums1)
        ctr2 = Counter(nums2)
        nums2 = set(nums2)
        
        divided = set()
        type_1 = 0
        for n in nums1:
            square = n * n
            for n2 in nums2:
                ctr_non_dup =0 
                ctr_dup = 0
                divisor = square / n2
                if divisor in nums2 and (divisor, n2) not in divided and (n2, divisor) not in divided:
                    divided.add((divisor, n2))
                    divided.add(n2)


                    if divisor != n2 and ctr2[n2] == 1 and ctr2[divisor] == 1:
                        ctr_non_dup += 1
                    if (ctr2[n2] > 1 or ctr2[divisor] > 1) and n2 != divisor:
                        ctr_non_dup = 1
                        
                        

                        
                        ctr_non_dup *= ctr2[n2] * ctr2[divisor]
                    if ctr2[n2] > 1 and n2 == divisor:
                        # 2 -> 1, 3-> 3, 4 -> 6
                        for i in range(ctr2[n2]):
                            ctr_dup += i
                        ctr_non_dup *= ctr2[n2] 
                    

                    ctr = ctr1[n] * (ctr_non_dup + ctr_dup)
                    type_1 += ctr
        divided = set()
        type_2 = 0

        for n in nums2:
            square = n * n
            for n2 in nums1:
                ctr_non_dup =0 
                ctr_dup = 0
                divisor = square / n2
                

                if divisor in nums1 and (divisor, n2) not in divided and (n2, divisor) not in divided:
                    divided.add((divisor, n2))


                    if divisor != n2 and ctr1[n2] == 1 and ctr1[divisor] == 1:
                        ctr_non_dup += 1
                    if n2 != divisor and (ctr1[n2] > 1 or ctr1[divisor] > 1):
                        ctr_non_dup = 1
                        

                        
                        ctr_non_dup *= ctr1[n2] * ctr1[divisor]
                    if ctr1[n2] > 1 and n2 == divisor:
                        
                        # 2 -> 1, 3-> 3, 4 -> 6
                        for i in range(ctr1[n2]):
                            ctr_dup += i
                        ctr_non_dup *= ctr1[n2] 

                    ctr = ctr2[n] * (ctr_non_dup + ctr_dup)
                    type_2 += ctr

        return type_1 + type_2
        



        

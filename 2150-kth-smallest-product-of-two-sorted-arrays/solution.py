import bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        mn = min(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        mx = max(nums1[0] * nums2[0], nums1[0] * nums2[-1], nums1[-1] * nums2[0], nums1[-1] * nums2[-1])
        med = mn

        def getLess(med):
            ct = 0
            for idx, n in enumerate(nums1):
                if n == 0:
                    if med >= 0:
                        ct += len(nums2)
                    else:
                        ct += 0
                else:
                    if n > 0:
                        ct += bisect.bisect(nums2, med / n)
                    else:
                        ct += len(nums2) - bisect.bisect_left(nums2, med / n)
            return ct

        while mn < mx:
            med = (mn + mx) // 2
            print("mn", mn, "mx", mx , "med", med)
            ct = getLess(med)
            print("ct", ct)
            if ct == k or (ct > k and getLess(med-1) < k):
                mn = med
             
                break
            elif ct < k:
                mn = med + 1
            else:
                mx = med - 1
        
        print("mn", mn)
        res = -float('inf')
        for idx, n in enumerate(nums1):
            if n == 0:
                if mn >= 0:
                    res = max(res, 0)
                continue
            cur_mx_idx = bisect.bisect(nums2, mn / n) - 1
            if n < 0:
                cur_mx_idx = bisect.bisect_left(nums2, mn / n)
                
            if cur_mx_idx < 0 or cur_mx_idx >= len(nums2):
                continue
            cur_mx = nums2[cur_mx_idx]
            if cur_mx * n <= mn:
                res = max(res, cur_mx * n)
        return res

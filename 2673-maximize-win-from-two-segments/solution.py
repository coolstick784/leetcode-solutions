class Solution(object):
    def maximizeWin(self, A, k):
        n = len(A)

        # best[t] = best window size we can get using only A[0 : t]
        best = [0] * (n + 1)

        left = 0
        answer = 0

        for right in range(n):
            # move left until the window fits in range k
            # (i.e., A[right] - A[left] <= k)
            while A[right] - A[left] > k:
                left += 1

            # size of the current valid window [left .. right]
            window_size = right - left + 1

            # best up to right+1 is either:
            # - best up to right (skip A[right])
            # - or take this window ending at right
            best[right + 1] = max(best[right], window_size)

            # combine:
            # - one window ending at right (size = window_size)
            # - plus the best window completely before index left
            answer = max(answer, window_size + best[left])

        return answer


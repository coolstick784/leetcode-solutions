class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        @lru_cache(None)
        def score(s_idx, m_idx):
            s = students[s_idx]
            m = mentors[m_idx]
            ans = 0
            for idx in range(len(s)):
                if s[idx] == m[idx]:
                    ans += 1
            return ans
        res = 0
        for p in permutations([n for n in range(len(mentors))]):
            cur = 0
            for s_idx, m_idx in enumerate(p):
                cur += score(s_idx, m_idx)
            res = max(res, cur)
        return res

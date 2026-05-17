class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        log_dict = {}
        for server, time in logs:
            log_dict.setdefault(time, []).append(server)

        times = sorted(log_dict.keys())
        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))

        ans = [0 for _ in queries]
        ctr = 0
        cur_servers = {}

        l = 0
        r = 0

        for q, original_idx in sorted_queries:
            while r < len(times) and times[r] <= q:
                t = times[r]
                for server in log_dict[t]:
                    cur_servers[server] = cur_servers.get(server, 0) + 1
                    if cur_servers[server] == 1:
                        ctr += 1
                r += 1

            while l < len(times) and times[l] < q - x:
                t = times[l]
                for server in log_dict[t]:
                    cur_servers[server] -= 1
                    if cur_servers[server] == 0:
                        ctr -= 1
                l += 1

            ans[original_idx] = n - ctr

        return ans

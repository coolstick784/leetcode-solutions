class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        cur_level = 0
        cur_list = set()
        new_list = set()
        new_list.add(id)
        explored = set()
        explored.add(id)
        while cur_level != level:
            cur_list = new_list.copy()  
            new_list = set()
            for i in cur_list:
                for f in friends[i]:
                    if f not in explored:
                        new_list.add(f)
                        explored.add(f)
            cur_level += 1

        res = {}
        for f in new_list:
            for m in watchedVideos[f]:
                res[m] = res.get(m, 0) + 1
        #print(res)
        final = [(ct, movie) for movie, ct in res.items()]
        return [movie for ct, movie in sorted(final)]

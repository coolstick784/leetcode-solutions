# we want to know the highest snap at or before the snap id, in a get, that the var was changed
# so when we set, we add the index and the value to a queue 
# and we'll initialize a dict with each index and the last time it was snapped
# then, we'll have a snaps dict, with every index and value at that snap


class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = {}
        self.index_dict = {}
        self.snap_id = 0
        for n in range(length):
            self.snaps.setdefault(-1, {})
            self.snaps[-1][n] = 0
            self.index_dict.setdefault(n, []).append(-1)
        self.cur_snaps = {}
        

    def set(self, index: int, val: int) -> None:
        self.cur_snaps[index] = val

    def snap(self) -> int:
        self.snaps[self.snap_id] = self.cur_snaps
        for n in self.cur_snaps:
            self.index_dict[n].append(self.snap_id)
        self.cur_snaps = {}
        self.snap_id += 1
        return self.snap_id-1
        

    def get(self, index: int, snap_id: int) -> int:
        most_recent = self.index_dict[index][bisect.bisect(self.index_dict[index], snap_id) - 1]
        return self.snaps[most_recent][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

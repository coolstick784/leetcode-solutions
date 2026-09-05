class ExamRoom:

    def __init__(self, n: int):
        self.next_right = {}
        
        self.next_left = {}
        
        self.n = n
        self.min_heap = []
        self.max_heap = []

        self.heap = []
        self.idxs = set()
        
        
        

    def seat(self) -> int:
        #print("idsxs", sorted(list(self.idxs)), self.heap)
        #print("heap", self.heap, "max heap", self.max_heap, "min heap", self.min_heap)
        mx_dist = float('inf')
        if self.heap:
            mx_dist, seat, real_dist = heapq.heappop(self.heap)
        while self.heap and (seat not in self.idxs or seat + real_dist != self.next_right[seat]):
            mx_dist, seat, real_dist = heapq.heappop(self.heap)
        if len(self.idxs) == 0:
            new_seat = 0
            heapq.heappush(self.min_heap, new_seat)
            heapq.heappush(self.max_heap, -new_seat)
            self.idxs.add(new_seat)
            return new_seat

        while self.max_heap and -self.max_heap[0] not in self.idxs:
            heapq.heappop(self.max_heap)
        while self.min_heap and self.min_heap[0] not in self.idxs:
            heapq.heappop(self.min_heap)
        dist_left = self.min_heap[0]
        dist_right = self.n-1 + self.max_heap[0]
        mx_dist *= -1 
        #print("dist left", dist_left, "mx dist", mx_dist, "dist right", dist_right)
        if dist_left >= mx_dist and dist_left >= dist_right:
            new_seat = 0
            if mx_dist != -float('inf'):
                heapq.heappush(self.heap, (-1*mx_dist, seat, real_dist))
            old_next = self.min_heap[0]
            self.next_right[new_seat] = old_next
            self.next_left[old_next] = new_seat
            heapq.heappush(self.heap, (-1 * ((old_next - new_seat) // 2), new_seat, (old_next-new_seat)))


        elif mx_dist >= dist_right:
            
            new_seat = seat + mx_dist
            old_next = self.next_right[seat]
            self.next_right[seat] = new_seat
            self.next_left[new_seat] = seat
            heapq.heappush(self.heap, (-1*((new_seat-seat)//2), seat, (new_seat-seat)))
            new_right = old_next
            self.next_right[new_seat] = new_right
            self.next_left[new_right] = new_seat
            heapq.heappush(self.heap, (-1*((new_right-new_seat)//2), new_seat, (new_right-new_seat)))

        else:
            new_seat = self.n - 1
            if mx_dist != -float('inf'):
                heapq.heappush(self.heap, (-1*mx_dist, seat, real_dist))
            old_left = -self.max_heap[0]
            self.next_right[old_left] = new_seat
            self.next_left[new_seat] = old_left
            heapq.heappush(self.heap, (-1 * ((new_seat - old_left) // 2), old_left, (new_seat - old_left)))
        

        

        
        print("new seat", new_seat)

        heapq.heappush(self.min_heap, new_seat)
        heapq.heappush(self.max_heap, -new_seat)
        self.idxs.add(new_seat)
        return new_seat

        

    def leave(self, p: int) -> None:
        while self.max_heap and -self.max_heap[0] not in self.idxs:
            heapq.heappop(self.max_heap)
        while self.min_heap and self.min_heap[0] not in self.idxs:
            heapq.heappop(self.min_heap)
        self.idxs.remove(p)
        
        prev_left = self.next_left.get(p, -float('inf'))
        prev_right = self.next_right.get(p, float('inf'))


        self.next_right[prev_left] = prev_right
        self.next_left[prev_right] = prev_left
        print("idsxs", sorted(list(self.idxs)), self.min_heap, self.max_heap)
        if prev_left != -self.max_heap[0] and prev_left != -float('inf') and prev_right != float('inf'):
            heapq.heappush(self.heap, (-1*((prev_right-prev_left)//2), prev_left, (prev_right-prev_left)))

        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)

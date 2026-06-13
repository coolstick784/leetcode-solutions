class EventManager:

    def __init__(self, events: list[list[int]]):
        self.priority = {} # for each priority have a heap
        self.cur = {}
        self.all = []
        self.id = 0
        for eventId, newPriority in events:
            self.updatePriority(eventId, newPriority)
        
    def updatePriority(self, eventId: int, newPriority: int) -> None:
        self.id += 1
        self.priority.setdefault(newPriority, [])
        heapq.heappush(self.priority[newPriority], eventId)
        self.cur[eventId] = self.id
        heapq.heappush(self.all, (-newPriority, eventId, self.id))
    def pollHighest(self) -> int:
        while self.all:
            cur, event, cur_id =heapq.heappop(self.all)
            cur = -cur
            
            
            if not self.priority[cur]:
                continue

            
            if self.cur[event] != cur_id:
                continue
            else:
                return event 

        return -1

        


# Your EventManager object will be instantiated and called as such:
# obj = EventManager(events)
# obj.updatePriority(eventId,newPriority)
# param_2 = obj.pollHighest()

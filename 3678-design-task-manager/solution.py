import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = {}
        self.highest = []
        self.all = set()
        for user, task, prio in tasks:
            self.tasks[task] = (prio, user)
            heapq.heappush(self.highest, (-prio, -task))
            self.all.add((-prio, -task))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.tasks[taskId] = (priority, userId)
        heapq.heappush(self.highest, (-priority, -taskId))
        self.all.add((-priority, -taskId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        prev_prio, prev_user = self.tasks[taskId]
        self.tasks[taskId] = (newPriority, prev_user)
        heapq.heappush(self.highest, (-newPriority, -taskId))
        self.all.remove((-prev_prio, -taskId))
        self.all.add((-newPriority, -taskId))
        
        

    def rmv(self, taskId: int) -> None:
        
        prev_prio, prev_user = self.tasks[taskId]
        del self.tasks[taskId]
        self.all.remove((-prev_prio, -taskId))

    def execTop(self) -> int:
        while self.highest and self.highest[0] not in self.all:
            heapq.heappop(self.highest)
        
        if not self.highest:
            return -1
        prio, task = heapq.heappop(self.highest)
        self.all.remove((prio, task))
      
        prio = -prio
        task = -task
        prio, user = self.tasks[task]
        del self.tasks[task]
        return user
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

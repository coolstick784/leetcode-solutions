"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if not head.next:

            res = Node(head.val, None, None)
            if head.random:
                res.random = res
            return res
        node = head
        ctr = 0
        random = {}
        mp = {}
        cur_random = {}
        while node:
            cur_random[ctr] = node.random
            random[ctr] = None

            node = node.next
            ctr += 1
        l = ctr
        node = head
        
        ctr = 0
        while node:
            for idx in cur_random:
                if node == cur_random[idx]:
                    print("ctr", ctr, "idx", idx)
                    random[idx] = ctr
            last = node
            node = node.next
            ctr += 1
        
        node = head
        cur = last
        ctr = 0
        while ctr < l and cur:
            cur.next = Node(node.val, None, None)
            
            new = node.next
            node.next = None
            node = new
            cur = cur.next
            if ctr == 0:
                res = cur
            mp[ctr] = cur
            
            ctr += 1
        node = res
        ctr = 0
        print("random", random)
        while node:
            random_map = random[ctr]

            node.random = mp.get(random_map) 
            node = node.next
            ctr += 1
        return res


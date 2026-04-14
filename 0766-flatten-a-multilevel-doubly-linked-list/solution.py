"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


# we have a head
# if there is no parent, no next, and no child, return the head
# if there is a parent, no next, and no child, set parent.next to the head, head.prev to the parent, and set node.next to the old parent.next, and old paretn.next.prev to the node
# if there is a child, set node.next to the child's head,  head.prev to the parent, and iterate through the child
# so at each point we want to know the old parent and old parent's next, as well as if there's a child
class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def solve(node, parent=None, parent_next=None):
            if not node:
                return 
            if not parent and not node.next and not node.child:
                return
            if parent and not node.next and not node.child:
                node.next = parent_next
                if parent_next:
                    parent_next.prev = node
                return 
            if node.child:
                node.child.prev = node
                solve(node.child, node, node.next)
                node.next = node.child
                node.child = None
            
            solve(node.next, parent, parent_next)
            return 
        solve(head)
        node = head

        return head

        

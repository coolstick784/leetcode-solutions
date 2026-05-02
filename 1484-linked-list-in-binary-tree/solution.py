# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        memo = {}
        def explore(node, need):
            if (id(node), id(need)) in memo:
                return memo[(id(node), id(need))]
            if not need:
                return True
            if not node:
                return False
    

            ans = False
            if node.val == need.val:
                if explore(node.left, need.next) or explore(node.right, need.next):
                    ans = True
            if not ans and node.val == head.val:
                if explore(node.left, head.next) or explore(node.right, head.next):
                    ans = True
            if not ans and (explore(node.left, head) or explore(node.right, head)):
                ans = True
            memo[(id(node), id(need))] = ans
            return ans
        

        return explore(root, head)

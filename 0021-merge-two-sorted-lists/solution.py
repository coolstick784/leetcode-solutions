# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_l1_node = list1
        cur_l2_node = list2
        start = None
        cur_node = None
        while(cur_l1_node is not None or cur_l2_node is not None):
            if cur_l1_node is None:
                if start == None:
                    start = ListNode(val=cur_l2_node.val, next=None)
                    cur_node = start
                    
                else:
                    cur_node.next = ListNode(val=cur_l2_node.val, next=None)
                    cur_node = cur_node.next
                cur_l2_node = cur_l2_node.next
            elif cur_l2_node is None:
                if start == None:
                    start = start = ListNode(val=cur_l1_node.val, next=None)
                    cur_node = start
                else:
                    cur_node.next = ListNode(val=cur_l1_node.val, next=None)
                    cur_node = cur_node.next
                cur_l1_node = cur_l1_node.next
            else:
                if cur_l1_node.val <= cur_l2_node.val:
                    if start == None:
                        start = start = ListNode(val=cur_l1_node.val, next=None)
                        cur_node = start
                    else:
                        cur_node.next = ListNode(val=cur_l1_node.val, next=None)
                        cur_node = cur_node.next
                    cur_l1_node = cur_l1_node.next
                else:
                    if start == None:
                        start = start = ListNode(val=cur_l2_node.val, next=None)
                        cur_node = start
                    else:
                        cur_node.next = ListNode(val=cur_l2_node.val, next=None)
                        cur_node = cur_node.next
                    cur_l2_node = cur_l2_node.next
            


        return start
        

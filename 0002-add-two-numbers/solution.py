# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getNumber(self, cur_list):
        len_list = len(cur_list)
        cur_list.reverse()
        out = 0
        for idx, n in enumerate(cur_list):
            out += 10 ** (len_list - idx - 1) * n

        return out
    def convertToList(self, listnode):
        out = []
        
        cur_node = listnode
        while cur_node.next is not None:
            out.append(cur_node.val)
            cur_node = cur_node.next
        out.append(cur_node.val)
        return out
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        converted_l1 = self.convertToList(l1)
        converted_l2 = self.convertToList(l2)
        n1 = self.getNumber(converted_l1)
        n2 = self.getNumber(converted_l2)
        final_number = n1 + n2
        out = list(str(final_number))

        out = [int(n) for n in out]
        
        cur_node = ListNode(out[0], None)
        for idx, n in enumerate(out[1:]):
            cur_node = ListNode(out[idx+1], cur_node) 

        return cur_node


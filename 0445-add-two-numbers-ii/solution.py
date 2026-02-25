# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ct_l1 = 0
        ct_l2 = 0
        cur_l1 = l1
        cur_l2 = l2
        while cur_l1 is not None:
            ct_l1 += 1
            cur_l1 = cur_l1.next
        while cur_l2 is not None:
            ct_l2 += 1
            cur_l2 = cur_l2.next
        
        cur_l1 = l1
        cur_l2 = l2
        out = ListNode(val=0)
        cur = out
        carries = [0]
        while ct_l1 > ct_l2:
            carries.append(0)
            cur.next = ListNode(val=cur_l1.val)

            cur_l1 = cur_l1.next
            cur = cur.next
            ct_l1 -= 1
        while ct_l2 > ct_l1:
            carries.append(0)
            cur.next = ListNode(val=cur_l2.val)
            cur_l2 = cur_l2.next
            cur = cur.next
            ct_l2 -= 1

        while ct_l1 > 0:
            cur_sum = cur_l1.val + cur_l2.val
            if cur_sum >= 10:
                carries.append(1)
                cur_sum -= 10
            else:
                carries.append(0)
            cur.next = ListNode(val=cur_sum)
            cur_l1 = cur_l1.next
            cur_l2 = cur_l2.next
            cur = cur.next
            ct_l1 -= 1
            ct_l2 -=1 
        cur = out

        # Carries should be [0, 0, 1] -> [10, 0] -> [1, 0, 0]
    
        while sum(carries) > 0 :
            new_carries = []

            cur = out
            for idx, carry in enumerate(carries[:-1]):
                cur.val += carries[idx+1]
                if cur.val >= 10:
                    new_carries.append(1)
                    cur.val -= 10
                else:
                    new_carries.append(0)
                cur = cur.next
            carries = new_carries.copy()
  
            
            
            
        
            
            
            
        if out.val > 0:
            return out
        return out.next
        
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        carry = 0

        
        cur_l1 = l1
        cur_l2 = l2
        while cur_l1 is not None or cur_l2 is not None:


            if cur_l1 is None:
                cur_sum = carry + cur_l2.val
                if cur_sum >= 10:
                    res.append(cur_sum - 10)
                    carry = 1
                    
                else:
                    res.append(cur_sum)
                    carry = 0
                    
                cur_l2 = cur_l2.next
            elif cur_l2 is None:
                cur_sum = carry + cur_l1.val
                if cur_sum >= 10:
                    res.append(cur_sum - 10 )
                    carry = 1
                    
                else:
                    res.append(cur_sum )
                    carry = 0
                    
                cur_l1 = cur_l1.next
            else:
                
                
                cur_sum = carry + cur_l1.val + cur_l2.val

                if cur_sum >= 10:
                    res.append(cur_sum - 10 )
                    carry = 1
                    
                else:
                    res.append(cur_sum )
                    carry = 0
                    
                cur_l1 = cur_l1.next
                cur_l2 = cur_l2.next
        if carry == 1:
            res.append(1)
            
        
        cur = ListNode(val=res[0])
        out = cur
       
        
        for idx, val in enumerate(res):
            
            if idx < len(res) - 1:
                cur.next = ListNode(val=res[idx+1])
            else:
                cur.next = None
            cur = cur.next
                
            
        return out
        

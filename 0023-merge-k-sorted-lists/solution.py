# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

  
        def convertToList(Node):
            
            out = []

            cur_node = Node
            while cur_node is not None:
                out.append(cur_node.val)
                cur_node = cur_node.next
            
            return out
        def convertToNode(l):

            l.reverse()
            if l == []:
                return None
            cur_node = ListNode(l[0], None)
            l = l[1:]
            while l != []:
                
                cur_node = ListNode(l[0], cur_node)
                l = l[1:]

            return cur_node

        out = []
        new_lists = [convertToList(Node) for Node in lists]
        while True:
            new_lists = [n for n in new_lists if n != []]


            if new_lists == []:


                return convertToNode(out)
            cur_vals = [n[0] for n in new_lists]
            min_val = min(cur_vals)
            min_idx = cur_vals.index(min_val)
            new_lists[min_idx] = new_lists[min_idx][1:]
            out.append(min_val)


        
        

        

# https://leetcode.com/problems/insertion-sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:




    # Dont work
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h=head
        
        p=head
        curVal=head.val
        
        itr=head
        while p:
            while itr.next and itr.next.val< curVal:
                itr.val=itr.next.val
                itr=itr.next

            itr.val=curVal
            p=p.next
            if p:
                curVal=p.val
            itr=p
        return h
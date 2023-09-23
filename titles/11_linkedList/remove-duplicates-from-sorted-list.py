# https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
                
        h=head
        cur=head
        if head:
            head=head.next        
        while head:
            print(head)
            while head and head.val==cur.val:                
                head=head.next
            cur.next=head
            
            cur=head
            if head:
                head=head.next
        return h

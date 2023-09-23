# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        mid=head
        back=mid
        
        head=head.next
        back.next=None
        while head:
            mid=head
            head=head.next
            mid.next=back
            back=mid
        return mid
            

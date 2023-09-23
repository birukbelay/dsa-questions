# https://leetcode.com/problems/reverse-linked-list-ii/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        before = self.getKth(head, left) if left>1 else dummy
        start=before.next
        if not start :
            return head
        
        
        ctr=left
        prev=start
        mid= start.next
        while mid and ctr<right:
            temp=mid.next
            mid.next=prev
            prev=mid
            mid=temp
            ctr+=1
        start.next=mid
        before.next=prev
        return dummy.next
        
    
    def getKth(self, cur, k):
        while cur and k>2:
            cur=cur.next
            k-=1
        return cur
        
        
        
        
        
        
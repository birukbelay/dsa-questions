
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        temp2=head
        ctr=0
        while temp:
            temp=temp.next
            ctr+=1
        # print(ctr)
        if ctr==1:
            return 
        if ctr==n:
            return head.next
        for i in range(ctr):
            
            if i==(ctr-n)-1:
                temp2.next=temp2.next.next
            if temp2:                
                temp2=temp2.next
        return head


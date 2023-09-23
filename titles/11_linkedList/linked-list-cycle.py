# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem
# https://leetcode.com/problems/linked-list-cycle/submissions/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        S = set()
        while head:
            if head in S:
                return 1
            else:
                S.add(head)
            head=head.next
        return 0
#         # using the tortoise and hare method       
#         flag = 0
#         slow = head
#         fast = head

#         while(fast and fast.next):
#             slow = slow.next
#             fast = fast.next.next
#             if (slow == fast):
#                 return 1        
#         else:
#             return 0
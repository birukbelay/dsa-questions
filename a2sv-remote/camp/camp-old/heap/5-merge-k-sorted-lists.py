# https://leetcode.com/problems/merge-k-sorted-lists/
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists) :
        heapArr=[]
        
        for nodes in lists:            
            while nodes:
                heapq.heappush(heapArr, nodes.val)
                nodes = nodes.next
        print(heapArr)
        listNode=ListNode()        
        temp=listNode
        while heapArr:
            listNode.next = ListNode(heapq.heappop(heapArr))
            listNode = listNode.next
        return temp.next
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenn = 0
        

    def get(self, index: int) -> int:
        if index >= self.lenn:
            return -1
        
        cur = self.head
        while index:
            cur = cur.next
            index -= 1
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new = Node(val)
        self.head, new.next = new, self.head
        if not self.tail:
            self.tail = self.head

        self.lenn += 1
        

    def addAtTail(self, val: int) -> None:
        new = Node(val)
        if self.head:
            self.tail.next, self.tail = new, new
        else:
            self.head = self.tail = new

        self.lenn += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.lenn:
            return
        elif index == self.lenn:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            index -= 1
            while index:
                cur = cur.next
                index -= 1

            new = Node(val)
            cur.next, new.next = new, cur.next

            self.lenn += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.lenn:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            i = index - 1
            while i:
                cur = cur.next
                i -= 1
        
            cur.next = cur.next.next
            if index == self.lenn - 1:
                self.tail = cur

        self.lenn -= 1
        if self.lenn == 0:
            self.head = self.tail = None
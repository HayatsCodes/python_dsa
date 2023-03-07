class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def insertEnd(self, val):
        self.tail.next = ListNode(val) 
    
    def remove(self, index):
        i = 0
        curr = self.head
        while i < index and cur:
            i += 1
            curr = curr.next
        if curr:
            curr.next = curr.next.next
    def print(self):
        curr = self.head.next
        while curr:
            print(curr.val, '->')
            curr = curr.next
        print()
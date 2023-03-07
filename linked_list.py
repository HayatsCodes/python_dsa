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
        i =0
        curr = self.head
        while curr.next != None
            curr = curr.next
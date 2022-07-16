class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# list 1
node4 = ListNode(-4, next=node2)
node3 = ListNode(0, next=node4)
node2 = ListNode(3, next=node3)
node1 = ListNode(2, next=node2)
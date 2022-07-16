class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# list 1
node3 = ListNode(4, next=None)
node2 = ListNode(2, next=node3)
node1 = ListNode(1, next=node2)

# list 2
node6 = ListNode(4, next=None)
node5 = ListNode(3, next=node6)
node4 = ListNode(1, next=node5)

# pointers
curr_node1 = node1
next_node1 = node1.next

curr_node2 = node4
next_node2 = node4.next

while curr_node1:
	while curr_node2:
		if curr_node1.val<curr_node2.val:
			curr_node1.next = curr_node2
			curr_node2 = curr_node1
			next_node2 = curr_node2.next
			curr_node1 = next_node1
			next_node1 = curr_node1.next
		
		else:
			if curr_node1.val >= curr_node2.val:
				if curr_node1.val >= next_node2.val:

			curr_node2.next = curr_node1
			curr_node1.next = curr_node2.next
			curr_node1 = next_node1
			next_node1 = curr_node1.next
			






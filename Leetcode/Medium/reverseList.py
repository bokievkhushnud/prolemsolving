class Node:
	def __init__(self, val=0, next=None):
		self.val: int = val
		self.next: Node = next

	# def __str__(self):
	# 	return str(self.val)

	def __repr__(self):
		print(self.val)
		return f'Node({self.val}, {self.next})'

# node3 = Node(3)
# node2 = Node(2, next=node3)
node = Node(1, next=None)

prev_node = node
current = node.next
prev_node.next = None
while current:
	old_next = current.next
	current.next = prev_node
	prev_node = current
	current = old_next


print(prev_node)
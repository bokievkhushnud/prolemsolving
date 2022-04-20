# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def addTwoNumbers(l1, l2):
        list_1 = [l1.val]
        list_2 = [l2.val]
        while l1.next!=None or l2.next!=None:
            try:
                list_1.append(l1.next.val)
                l1 = l1.next
            except Exception as e:
                list_2.append(l2.next.val)
                l2 = l2.next
     
        num1 = int(''.join([str(i) for i in list_1[::-1]]))
        num2 = int(''.join([str(i) for i in list_2[::-1]]))
        result = num1+num2
        new_list = [int(i) for i in str(result)]
        new_list = list(reversed(new_list))
        result = ListNode(new_list[0])
        result_tail = result
        for i in new_list[1:]:
            result_tail.next = ListNode(i) 
            result_tail = result_tail.next
        return result

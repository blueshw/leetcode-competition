# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(-1)
        while l1 or l2:
            l1_value, l2_value = 0, 0
            if l1:
                l1_value = l1.val
            if l2:
                l2_value = l2.val
            value = l1_value + l2_value
            
            if node and node.next:
                value += node.next.val
            
            save_value = value % 10
            next_value = -1
            if value >= 10:
                next_value = int(value / 10)
            
            if node.next or (node.val > -1 and not node.next):
                node.next = ListNode(save_value)
                node = node.next
            else:
                node.val = save_value
                    
            if next_value > 0:
                node.next = ListNode(next_value)
            
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        return head
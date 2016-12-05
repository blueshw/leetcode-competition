# Definition for singly-linked list.
# class ListNode(object):
 #   def __init__(self, x):
 #       self.val = x
 #       self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_node = ListNode(0)
        sum_node = ret_node
        upper = 0
        while True:
            if l1 is None and l2 is None:
                if upper == 1:
                    sum_node.next = ListNode(1)
                return ret_node.next
    
            
            sum_val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0)
            if upper == 1:
                sum_val += 1
                upper = 0
                
        
            upper = 1 if sum_val >= 10 else 0
            sum_val = sum_val % 10
            
            
            sum_node.next = ListNode(sum_val)
            sum_node = sum_node.next
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

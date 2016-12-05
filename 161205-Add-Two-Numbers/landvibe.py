class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        output = ListNode(0)
        current = output
        while True:
            val = current.val
            if l1 is not None:
                val += l1.val
            if l2 is not None:
                val += l2.val
            current.val = val % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 is None and l2 is None:
                if val >= 10:
                    current.next = ListNode(1)
                return output
            current.next = ListNode(1 if val >= 10 else 0)
            current = current.next
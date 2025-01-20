from Node import Node

class MergeSort:
    def __init__(self, head):
        self.sorted_head = self._mergeSort(head)


    def _mergeSort(self, head):
        if not head or not head.next:
            return head

        mid = self._split(head)
        left = self._mergeSort(head)
        right = self._mergeSort(mid)
        
        return self._merge(left, right)


    def _split(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        return mid


    def _merge(self, left, right):
        tmp = Node()
        tail = tmp
        while left and right:
            if left.value < right.value:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        return tmp.next
        
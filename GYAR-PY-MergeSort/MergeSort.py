from Node import Node

class MergeSort:
    @staticmethod
    def mergeSort(head):
        if not head or not head.next:
            return head

        mid = MergeSort._split(head)
        left = MergeSort.mergeSort(head)
        right = MergeSort.mergeSort(mid)
        
        return MergeSort._merge(left, right)


    def _split(head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        return mid


    def _merge(left, right):
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
        
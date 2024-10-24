from Node import Node

class List:   
    def __init__(self, head = None):
        if head is not None:
            self.Head = Node(head)
        else:
            self.head = None 


    def push(self, input):
        if (self.head == None):
            self.head = Node(input)
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = Node(input)


    def pushAt(self, index):
        if index < 0 or index > self.getSize():
            print(f"Push index {index} out of range")
            return

        push = Node(input)
        if index == 0:
            push.next = head
            head = push
            return
        current = self.head
        for i in range(index-1):
            current = current.next
        push.next = current.next
        current.next = push.next


    def pull(self, index):
        current = self.head
        for i in range(index):
            if (current.next == None):
                return None
            current = current.next
        return current.value
    

    def removeElement(self, index):
        if index < 0 or index > self.getSize() - 1:
            print(f"Element index {index} out of range")
            return
        
        if not head:
            print("List is empty")
        elif index == 0:
            tmp = self.head
            head = head.next
            del tmp
        else:
            current = self.head
            previus = None
            for i in range(index):
                previus = current
                current = current.next
            previus.next = current.next
            del current


    def getSize(self):
        current = self.head
        size = 0
        while(current):
            size += 1
            current = current.next
        return size
    

    def printElement(self, index):
        if (index < 0):
            print("index can't be negative")
            return
        if not self.head: #if (not self.head):        
            print("List is empty")
        else:
            current = self.head
            for i in range(index):
                if (current.next == None):
                    print(f"Index {index} is out of range")
                    return
                current = current.next
            print(f"Element {index} value: {current.value}")
    

    def printLast(self):
        #if self.head is not None:
        if self.head:
            current = self.head
            while current.next is not None:
                current = current.next
            print(current.value)
        else:
            print("List is empty")


    def printFirst(self):
        if self.head is not None:
            print(self.head)
        else:
            print("list is empty")
    

    def printAll(self):
        if self.head is not None:
            current = self.head
            while current is not None:
                print(current.value)
                current = current.next
        else:
            print("List is empty")
    

    def boubbleSort(self):
        size = self.getSize()
        if size < 2:
            return
        #current = None
        #temporary = None
        for i in range(size-1):
            currenct = self.head
            for j in range(size - i - 1):
                if current.next is None:
                    break
                if current.value > current.next.value:
                    temporary = current.value
                    current.value = current.next.value
                    current.next.value = temporary
                current = current.next 


    #def mergeSort(self):

    #def _mergeSort_(self):

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_last(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        print(count)

    def remove_at(self, index):
        if index < 0 | index >= self.head.get_length():
            raise Exception("Not in range")
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 | index >= self.head.get_length():
            raise Exception("Not in range")
        if index == 0:
            self.insert_first(data)

        count = 0
        itr = self.head
        while itr:

            if index - 1 == count:
                node = Node(data, itr.next)
                itr.next = node

            itr = itr.next
            count += 1


    def print(self):
        if self.head is None:
            print('list is empty')
            return

        itr = self.head
        lstr = ''
        while itr:
            lstr += str(itr.data) + '---->'
            itr = itr.next

        print(lstr)

    def reverse(self):
        current = self.head
        newLinkedList = None
        while current:
           next_node=current.next
           current.next=newLinkedList
           newLinkedList=current
           current=next_node
        self.head=newLinkedList








ll = LinkedList()
ll.insert_values([1,2,3,4,5])
ll.print()
ll.reverse()
ll.print()
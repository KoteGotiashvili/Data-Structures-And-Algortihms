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

    def reverse(self, current):
        if current is None or current.next is None:
            #set last element to first element, head
            self.head=current
            return
        self.reverse(current.next) # call recursively in order to get last element
        # next means next pointer 6 this->this 5 next does not mean None next.next means pointer after 5 for example
        current.next.next = current
        current.next = None

    # Merge two sorted LinkedList
    def merge(self,current_a, current_b):
        # After some value is none it is returned from call stack
        if current_a is None:
            return current_b
        if current_b is None:
            return current_a
        if current_a.data < current_b.data:
            # After some value is none it is returned from call stack and assigned here using next. it does backpropagation of functions
            # like this 1 -> merge(2,100), 1-> merge(3,100) and then sets returned values from functions
            # It re assigning pointers from call stack
            current_a.next = self.merge(current_a.next, current_b) # backs there returned values from call stack
            return current_a
        else:
            current_b.next = self.merge(current_a, current_b.next) # here to its returns based on call stack and output and sets using next pointer
            return current_b





ll = LinkedList()

ll_1 = LinkedList()
ll.insert_values([1,2,3,4,5])
ll_1.insert_values([100,200,300,400,500])
ll.print()
ll.merge(ll.head, ll_1.head)
ll.print()
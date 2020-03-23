from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    def push(self, value):
        # adding to a stack adds on the end
        self.storage.add_to_tail(value)
        self.size +=1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            value = self.storage.remove_from_tail()
        else:
            value = None
        return value

    def len(self):
        return self.size

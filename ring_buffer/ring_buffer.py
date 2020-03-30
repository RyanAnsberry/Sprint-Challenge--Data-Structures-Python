from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if length of DLL is less than capacity
        if len(self.storage) < self.capacity:
            # add node with item value to tail of DLL
            self.storage.add_to_tail(item)
        # if current is None 
        elif self.current is None:
            # set current to the head
            self.current = self.storage.head
            # assign item to current's value
            self.current.value = item
            # set current to next node
            self.current = self.current.next
        else:
            # assign item to current's value
            self.current.value = item
            # set current to next node
            self.current = self.current.next
            

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        # set a var to iterate through DLL
        curr_node = self.storage.head
        # iterate through DLL
        while curr_node is not None:
            # append DLL values to list
            list_buffer_contents.append(curr_node.value)
            # set curr to next node
            curr_node = curr_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.curr_index = 0

    def append(self, item):
        # check if curr index is less than capacity
        if self.curr_index < self.capacity:
            # add item to current index and iterate to the nest
            self.storage[self.curr_index] = item
            self.curr_index += 1
        else: 
            # reset curr index to the beginning
            # before adding next item
            self.curr_index = 0
            self.storage[self.curr_index] = item
            self.curr_index += 1

    def get(self):
        # arr to hold values != None
        arr = []
        # iterate through storage
        for i in self.storage:
            # if not none add it to arr
            if i:
                arr.append(i)
        return arr








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
        pass

    def append(self, item):
        pass

    def get(self):
        pass

buffer = RingBuffer(3)

print(f"Should return [] : {buffer.get()}")

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(f"Should return ['a', 'b', 'c'] : {buffer.get()}")

buffer.append('d')

print(f"Should return ['d', 'b', 'c'] : {buffer.get()}")

buffer.append('e')
buffer.append('f')

print(f"Should return ['d', 'e', 'f'] : {buffer.get()}")


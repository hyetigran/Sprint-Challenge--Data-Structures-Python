from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.current is None:
            self.current = self.storage.head

        if self.storage.length == self.capacity and self.current == self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.current.next

        elif self.storage.length == self.capacity and self.current == self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.storage.head
        
        elif self.storage.length >= self.capacity:
            self.current.insert_before(item)
            self.storage.length += 1
            temp = self.current.next
            self.storage.delete(self.current)
            self.current = temp
        else:
            self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        temp = self.storage.head
        list_buffer_contents.append(temp.value)

        while temp is not self.storage.tail:
            temp = temp.next
            list_buffer_contents.append(temp.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

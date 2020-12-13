class Node:
    """
    Define Singly Linked List node class.
    Contructor takes in the node value, and
    next node pointer or null.
    """

    def __init__(self, value, next=None):
        self._value = value
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def get_node(self, position):
        if not self._head:
            return None
        temp_node = self._head
        count = 0
        while temp_node and count < position:
            temp_node = temp_node._next
            count += 1
        return temp_node

    def add_to_tail(self, value):
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
        self._length += 1
        return self

    def add_to_head(self, value):
        node = Node(value)
        if not self._head:
            self._head = node
            self._tail = node
        else:
            node._next = self._head
            self._head = node
        self._length += 1
        return self

    def remove_head(self):
        if not self._head:
            return None
        old_head = self._head
        self._head = self._head._next
        self._length -= 1
        return old_head

    def remove_tail(self):
        if not self._head:
            return None
        old_tail = self._head
        new_tail = self._head
        while old_tail is not self._tail:
            new_tail = old_tail
            old_tail = old_tail._next
        new_tail._next = None
        self._tail = new_tail
        self._length -= 1
        if self._length < 1:
            self._head = None
            self._tail = None
        return old_tail

    def __len__(self):
        return self._length

# Phase 2

    # TODO: Implement the contains_value method here
    def contains_value(self, target):
        if not self._head:
            return None
        temp_node = self._head
        while temp_node and temp_node._value != target:
            temp_node = temp_node._next
        return temp_node

    # TODO: Implement the insert_value method here
    def insert_value(self, position, value):
        if position > self._length:
            return None
        elif position == self._length:
            self.add_to_tail(value)
            return
        elif position == 0:
            self.add_to_head
            return
        else:
            node = Node(value)
            temp_node = self._head
            count = 1
            while temp_node and count < position:
                temp_node = temp_node._next
                count += 1
            node._next = temp_node._next
            temp_node._next = node
            self._length += 1
            return self

    # TODO: Implement the update_value method here
    def update_value(self, position, value):
        if position > self._length:
            return None
        count = 0
        temp_node = self._head
        while temp_node and count < position:
            temp_node = temp_node._next
        temp_node._value = value
        return self

    # remove any node method
    def remove_node(self, position):
        if position > self._length:
            return None
        if position == 0:
            self.remove_head()
            return
        if position == self._length:
            self.remove_tail()
            return
        temp_node = self._head
        previous_node = self._head
        count = 0
        while temp_node and count < position:
            previous_node = temp_node
            temp_node = temp_node._next
        previous_node._next = temp_node._next
        self._length -= 1
        return temp_node

    # class __str__ method
    def __str__(self):
        if not self._length:
            return 'Empty list.'
        string = ''
        temp_node = self._head
        while temp_node:
            string += temp_node._value
            temp_node = temp_node._next
            if temp_node:
                string += ', '
        return string


# Phase 1 Manual Testing:
# 1. Test Node and LinkedList initialization
node = Node('hello')
# <__main__.Node object at ...>
print('126', node)
print('127', node._value)                              # hello
linked_list = LinkedList()
# <__main__.LinkedList object at ...>
# print(linked_list)

# # 2. Test getting a node by its position
print('133', linked_list.get_node(0))                # None

# # 3. Test adding a node to the list's tail
linked_list.add_to_tail('new tail node')
# <__main__.Node object at ...>
print('137', linked_list.get_node(0))
print('138', linked_list.get_node(0)._value)         # `new tail node`

# # 4. Test adding a node to list's head
linked_list.add_to_head('new head node')
# <__main__.Node object at ...>
print('142', linked_list.get_node(0))
print('143', linked_list.get_node(0)._value)         # `new head node`

# # 5. Test removing the head node
linked_list.remove_head()
# `new tail node` because `new head node` has been removed
print('148', linked_list.get_node(0)._value)
# `None` because `new head node` has been removed
print('150', linked_list.get_node(1))

# # 6. Test removing the tail node
print('165', linked_list.get_node(0)._value)         # `new tail node`
linked_list.remove_tail()
print('167', linked_list.get_node(0))                # None

# # 7. Test returning the list length
print('170', len(linked_list))                                 # 0
print('167', linked_list.get_node(0))  # None
# Phase 2 Manual Testing

# # 1. Test whether the list contains_value a value
linked_list = LinkedList()
linked_list.add_to_head('new head node')
print('213', linked_list.contains_value('new head node'))      # True
print('214', linked_list.contains_value('App Academy node'))   # False

# # 2. Test inserting a node value into the list at a specific position
linked_list.insert_value(0, 'hello!')
print('218', linked_list.get_node(0)._value)                   # `hello!`

# # 3. Test updating a list node's value at a specific position
linked_list.update_value(0, 'goodbye!')
print('222', linked_list.get_node(0)._value)                   # `goodbye!`

# # 4. Test removing a node value from the list at a specific position
# `new head node`
print('225', linked_list.get_node(0)._value)
linked_list.remove_node(1)
print('227', linked_list.get_node(1))                          # None

# # 5. Format the list as a string whenever `print()` is invoked
new_linked_list = LinkedList()
print('231', new_linked_list)                  # Empty List
new_linked_list.add_to_tail('puppies')
print('233', new_linked_list)                  # puppies
new_linked_list.add_to_tail('kittens')
print('235', new_linked_list)                  # puppies, kittens

#!/usr/bin/python3
def sorted_insert(self, value):
    """Insert a new node to SinglyLinkedList.
    The node is inserted into the list at the correct
    ordered numerical position.
    Args:
        value (int): The value of the new Node to insert.
    """
    new_item = Node(value)
    if self.__head is None:
        new_item.next_node = None
        self.__head = new_item
    elif self.__head.data > value:
        new_item.next_node = self.__head
        self.__head = new_item
    else:
        template = self.__head
        while (template.next_node is not None and
                template.next_node.data < value):
            template = template.next_node
        new_item.next_node = template.next_node
        template.next_node = new_item

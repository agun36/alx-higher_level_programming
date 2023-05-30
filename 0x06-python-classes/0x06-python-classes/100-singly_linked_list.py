#!/usr/bin/python3
"""define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """create a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinked_List."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to  Singly_Linked_List.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new_item = Node(value)
        if self.__head is None:
            new_item.next_node = None
            self.__head = new
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

    def __str__(self):
        """Define the print of a Singly_LinkedList."""
        values = []
        template = self.__head
        while template is not None:
            values.append(str(template.data))
            template = template.next_node
        return ('\n'.join(values))

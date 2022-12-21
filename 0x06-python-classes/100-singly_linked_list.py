#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
  """This is a Node class"""
  
  def __init__(self, data, next_node=None):
    """Instantiate a new Node
    
    Args:
      data (int): Data of the new Node
      next_node (Node): Next Node to the new Node
    """
    self.__data = data
    self.__next_node = next_node
  
  @property
  def data(self):
    """Returns data of node"""
    return self.__data
  
  @data.setter
  def data(self, value):
    """Set the value for data of node"""
    if not isinstance(value, int):
      raise TypeError("data must be an integer")
    self.__data = value
    
  @property
  def next_node(self):
    """Returns next node of current node"""
    return self.__next_node
  
  @next_node.setter
  def next_node(self, value):
    """Set the value for next node"""
    if not isinstance(value, Node) or value is not None:
      raise TypeError("next_node must be a Node object")
    self.__next_node = value
    
    
    
class SinglyLinkedList:
  """This is a singly linked list"""
  
  def  __init__(self):
    """Initialize a singly linked list"""
    
    self.__head = None
    
  def sorted_insert(self, value):
    """Insert a new Node to the SinglyLinkedList.
    
    The node is inserted into the list at the correct
    ordered numerical position.
    
    Args:
    value (Node): The new Node to insert.
    """
    new = Node(value)
    if self.__head is None:
        new.next_node = None
        self.__head = new
    elif self.__head.data > value:
        new.next_node = self.__head
        self.__head = new
    else:
        tmp = self.__head
        while (tmp.next_node is not None and
                tmp.next_node.data < value):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

  def __str__(self):
      """Define the print() representation of a SinglyLinkedList."""
      values = []
      tmp = self.__head
      while tmp is not None:
          values.append(str(tmp.data))
          tmp = tmp.next_node
      return ('\n'.join(values))

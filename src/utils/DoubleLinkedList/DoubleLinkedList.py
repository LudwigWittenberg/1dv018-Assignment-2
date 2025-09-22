from src.utils.DoubleLinkedList.DLList import DLList

class DoubleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.cnt = 0
    
  def add_first(self, value):
    self.cnt += 1
    new_node = DLList(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.head.prv = new_node
      new_node.nxt = self.head
      self.head = new_node
      
  def add_last(self, value):
    self.cnt += 1
    new_node = DLList(value)
    if self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.nxt = new_node
      new_node.prv = self.tail
      self.tail = new_node
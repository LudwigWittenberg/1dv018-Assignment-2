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
      
  def remove_first(self):
    if self.head is not None:
      self.cnt -= 1
      if not self._is_head_tail_same():
        self.head.nxt.prev = None
        self.head = self.head.nxt
        
  def remove_last(self):
    if self.tail is not None:
      self.cnt -= 1
      
      if not self._is_head_tail_same():
        self.tail.prv.nxt = None
        self.tail = self.tail.prv
        
  def _is_head_tail_same(self):
    if self.head == self.tail:
      self.head = None
      self.tail = None
      return True
    
    # If head and tail are not the same
    return False
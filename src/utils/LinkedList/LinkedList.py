from src.utils.LinkedList.LList import LList

class LinkedList:
  def __init__(self):
    self.head = None
    self.cnt = 0
    self.tail = None
    
  def append(self, value):
    self.cnt += 1
    if self.head is None:
      self.head = LList(value)
      self.tail = self.head
    else:
      self.tail.nxt = LList(value)
      self.tail = self.tail.nxt
      
  def pop(self, value_to_remove):
    if self.head is None:
      raise ValueError("Value not found in list")
    
    if self.head.value == value_to_remove:
      self.head = self.head.nxt
      if self.head is None:
        self.tail = None
      self.cnt -= 1
      return

    current = self.head
    while current.nxt is not None and current.nxt.value != value_to_remove:
      current = current.nxt
    
    if current.nxt is None:
      raise ValueError("Value not found in list")
    
    current.nxt = current.nxt.nxt
    if current.nxt is None:
      self.tail = current
    self.cnt -= 1

  def get_count(self):
    return self.cnt
  
  def empty(self):
    return self.cnt == 0

  def __len__(self):
    return self.cnt
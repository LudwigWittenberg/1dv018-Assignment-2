from src.utils.LinkedList.DLList import DLList

class LinkedList:
  def __init__(self):
    self.head = None
    self.cnt = 0
    self.tail = None
    
  def append(self, value):
    self.cnt += 1
    if self.head is None:
      self.head = DLList(value)
      self.tail = self.head
    else:
      self.tail.nxt = DLList(value)
      self.tail = self.tail.nxt

  def get_count(self):
    return self.cnt
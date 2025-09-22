from src.utils.LinkedList.DLList import DLList

class LinkedList:
  def __init__(self):
    self.head = None
    self.cnt = 0
    self.last = None
    
  def append(self, value):
    self.cnt += 1
    if self.head is None:
      self.head = DLList(value)
      self.last = self.head
    else:
      self.last.nxt = DLList(value)
      self.last = self.last.nxt

  def get_count(self):
    return self.cnt
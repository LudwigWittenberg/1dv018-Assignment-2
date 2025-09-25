from src.utils.LinkedList.LList import LList

class HTSC:
  def __init__(self, size=5):
    self.size = size
    self.table = [None] * self.size
    
  def insert(self, value):
    hash_index = hash(value) % self.size
    self.table[hash_index] = self._insert_chain(self.table[hash_index], value)
    
  def _insert_chain(self, node, value):
    if node is None:
      return LList(value)
    
    node.nxt = self._insert_chain(node.nxt, value)
    
    return node
  
  def find(self, value):
    hash_index = hash(value) % self.size

    if self.table[hash_index] is not None:
      position = self.table[hash_index]
      
      while position is not None:
        if position.value == value:
          return True
        position = position.nxt
        
    return False
  
  def __len__(self):
    count = 0
    
    for place in self.table:
      count += self._count_chain(place)
      
    return count
  
  def _count_chain(self, node):
    count = 0
    
    while node is not None:
      count += 1
      node = node.nxt
    
    return count

  def count_conflicts(self):
    each_conflict = []
    
    for col in self.table:
      count = 0
      
      if col is not None and col.nxt is not None:
        count += self._count_chain(col) - 1
      
      each_conflict.append(count)
        
    return each_conflict
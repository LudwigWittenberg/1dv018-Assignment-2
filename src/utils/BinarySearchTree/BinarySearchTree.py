from src.utils.BinarySearchTree.BNode import BNode

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def add(self, key):
     self.root = self._add(self.root, key)
     
  def _add(self, node, key):
    if node is None:
      return BNode(key)

    if key < node.value:
      node.left = self._add(node.left, key)
    else:
      node.right = self._add(node.right, key)

    return node
  
  def remove(self, key):
    self.root = self._remove(self.root, key)
    
  def _remove(self, node, key):
    if node is None:
      return None

    if key < node.value:
      node.left = self._remove(node.left, key)
    elif key > node.value:
      node.right = self._remove(node.right, key)
    else:
      if node.left is None:
        return node.right
      elif node.right is None:
        return node.left

      min_larger_node = self._get_min(node.right)
      node.value = min_larger_node.value
      node.right = self._remove(node.right, min_larger_node.value)

    return node
  
  def _get_min(self, node):
    if node.left is None:
      return node
    else:
      return self._get_min(node.left)
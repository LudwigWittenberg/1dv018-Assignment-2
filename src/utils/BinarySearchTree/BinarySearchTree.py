from src.utils.BinarySearchTree.BNode import BNode

class BinarySearchTree:
  def __init__(self):
    self.root = None
    self.cnt = 0

  def add(self, key):
    self.root = self._add(self.root, key)
    self.cnt += 1
     
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
    self.cnt -= 1
    
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
    
  def height(self):
    return self._height(self.root)
  
  def _height(self, node):
    if node is None:
      return -1
    else:
      left_height = self._height(node.left)
      right_height = self._height(node.right)
      return 1 + max(left_height, right_height)
    
  def size(self):
    return self.cnt
  
  def __contains__(self, key):
    return self._contains(self.root, key)
  
  def _contains(self, node, key):
    if node is None:
      return False

    if node.value > key:
      return self._contains(node.left, key)
    elif node.value < key:
      return self._contains(node.right, key)
    else:
      return True
    
  def in_order(self, node):
    if node is None:
      return ''
    else:
      s = self.in_order(node.left)
      s += f' {node.value} '
      s += self.in_order(node.right)
      return s
    
  def pre_order(self, node):
    if node is None:
      return ''
    else:
      s = f' {node.value} '
      s += self.pre_order(node.left)
      s += self.pre_order(node.right)
      return s
    
  def post_order(self, node):
    if node is None:
      return ''
    else:
      s = self.post_order(node.left)
      s += self.post_order(node.right)
      s += f' {node.value} '
      return s
from src.utils.BinarySearchTree.BinarySearchTree import BinarySearchTree

def Task3():
  bst = BinarySearchTree()
  bst.add(3)
  
  bst.add(1)
  bst.add(4)
  bst.add(2)
  print("Binary Search Tree created with root:", bst.root.value)
  
  print("Removing 3 from the Binary Search Tree")
  bst.remove(3)
  print("New root after removing 3:", bst.root.value)
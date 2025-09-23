from src.utils.BinarySearchTree.BinarySearchTree import BinarySearchTree

def Task3():
  bst = BinarySearchTree()
  bst.add(4)
  
  bst.add(3)
  bst.add(1)
  bst.add(2)
  bst.add(5)
  bst.add(6)
  # print("Binary Search Tree created with root:", bst.root.value)
  
  # print(bst.size())
  # # print("Removing 3 from the Binary Search Tree")
  # # bst.remove(3)
  # print("New root after removing 3:", bst.root.value)
  # print("Current size of the Binary Search Tree:", bst.size())
  
  # print("Height of the Binary Search Tree:", bst.height())
  
  # print("Does the Binary Search Tree contain 4?", 4 in bst)
  
  # print("Does the Binary Search Tree contain 3?", 3 in bst)

  print("inorder traversal of the Binary Search Tree:", bst.in_order(bst.root))

  # print("preorder traversal of the Binary Search Tree:", bst.pre_order(bst.root))

  # print("postorder traversal of the Binary Search Tree:", bst.post_order(bst.root))
  
  bst.special_operation(5)
  
  print("inorder traversal of the Binary Search Tree:", bst.in_order(bst.root))
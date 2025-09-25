from src.utils.BinarySearchTree.BinarySearchTree import BinarySearchTree
from src.utils.GetRadomNumbers import get_x_random_numbers, get_random_number

def Task3():
  bst = BinarySearchTree()
  
  print("Current size of the Binary Search Tree:", bst.size())
  print("")

  print("Adding 10 random numbers to the Binary Search Tree")
  random_numbers = get_x_random_numbers(20, 10)
  
  for number in random_numbers:
    bst.add(number)
    
  print()
  print("Current size of the Binary Search Tree:", bst.size())
  print("Height of the Binary Search Tree:", bst.height())
  print("inorder traversal of the Binary Search Tree:", bst.in_order(bst.root))
  print("preorder traversal of the Binary Search Tree:", bst.pre_order(bst.root))
  print("postorder traversal of the Binary Search Tree:", bst.post_order(bst.root))
  print()
  
  amount_of_operations = get_random_number(6) // 2 + 1
  
  print("Removing", amount_of_operations, "numbers from the Binary Search Tree")
  
  for _ in range(amount_of_operations):
      in_order_string = bst.in_order(bst.root)
      in_order_list = [int(x) for x in in_order_string.split() if x.strip()]
      
      if len(in_order_list) == 0:
          print("No more elements to remove")
          break
          
      random_index = get_random_number(len(in_order_list) - 1)
      number_to_remove = in_order_list[random_index]
      
      print("Random index: ",{random_index}, "List length: ", len(in_order_list))
      print("Removing", number_to_remove)
      
      bst.remove(number_to_remove)
    
  print()
  print("Current size of the Binary Search Tree:", bst.size())
  print("Height of the Binary Search Tree:", bst.height())
  print("inorder traversal of the Binary Search Tree:", bst.in_order(bst.root))
  print("preorder traversal of the Binary Search Tree:", bst.pre_order(bst.root))
  print("postorder traversal of the Binary Search Tree:", bst.post_order(bst.root))
  print("")
  
  print("Performing special operation, removing the third largest element")
  bst.special_operation(3)
  print("inorder traversal of the Binary Search Tree after special operation:", bst.in_order(bst.root))
    
  
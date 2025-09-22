from src.utils.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList

def Test_Task2():
  print("")
  print("Running tests for Task 2...")
  _raise_error_list_empty_head()
  _raise_error_list_empty_tail()
  _list_correct_length_and_empty()
  print("All tests passed!")
  
def _raise_error_list_empty_head():
  dll = DoubleLinkedList()
  assert dll.size() == 0
  assert dll.is_empty() == True
  try:
    dll.remove_first()
  except Exception as e:
    assert str(e) == "List is empty"

def _raise_error_list_empty_tail():
  dll = DoubleLinkedList()
  try:
    dll.remove_last()
  except Exception as e:
    assert str(e) == "List is empty"
    
def _list_correct_length_and_empty():
  dll = DoubleLinkedList()
  assert dll.size() == 0
  assert dll.is_empty() == True
  dll.add_first(1)
  assert dll.size() == 1
  assert dll.is_empty() == False
  dll.add_last(2)
  assert dll.size() == 2
  assert dll.is_empty() == False
  dll.remove_first()
  assert dll.size() == 1
  assert dll.is_empty() == False
  dll.remove_last()
  assert dll.size() == 0
  assert dll.is_empty() == True
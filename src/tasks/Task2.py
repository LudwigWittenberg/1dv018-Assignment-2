from src.utils.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList
from src.utils.GetRadomNumbers import get_random_number

def Task2():
  # Selects a random number between 3 and 20
  # Used as the amount of numbers to add to the linked list
  while True:
    amount_of_numbers = get_random_number(20)
    if amount_of_numbers > 3 and amount_of_numbers % 2 == 0:
      break

  dll = DoubleLinkedList()
  
  # Just to show that it works, adding a number before adding random numbers
  dll.add_first(3)
  
  print("Current dll before adding:")
  print_current_dll(dll)
  print("")

  print("Number of elements to add:", amount_of_numbers)
  print("")
  
  # Add half of the numbers to the start of the DLL and half to the end
  amount_of_numbers //= 2

  print("Adding", amount_of_numbers, "numbers to the end of the DLL")
  for _ in range(amount_of_numbers):
    dll.add_last(get_random_number(100))

  print("Current DLL after adding to the end:")
  print_current_dll(dll)
  print("")

  print("Adding", amount_of_numbers, "numbers to the start of the DLL")
  for _ in range(amount_of_numbers):
    dll.add_first(get_random_number(100))

  print("Current DLL after adding to the start:")
  print_current_dll(dll)
  print("")

  print("Current DLL size:", dll.size())
  print("Is DLL empty?", dll.is_empty())
  print("")

  # Add half of the numbers to the start of the DLL and half to the end
  amount_of_numbers //= 2

  print("Removing ", amount_of_numbers, "numbers from the start of the DLL")
  for _ in range(amount_of_numbers):
    dll.remove_first()

  print("Current DLL after removing from the start:")
  print_current_dll(dll)
  print("")

  print("Removing", amount_of_numbers, "numbers from the end of the DLL")
  for _ in range(amount_of_numbers):
    dll.remove_last()

  print("Current DLL after removing from the end:")
  print_current_dll(dll)
  print("")

  print("Current DLL size:", dll.size())
  print("Is DLL empty?", dll.is_empty())
  
def print_current_dll(dll):
  current = dll.head
  values = []
  while current is not None:
    values.append(str(current.value))
    current = current.nxt
  print(" -> ".join(values))

import numbers
from src.utils.LinkedList.LinkedList import LinkedList
from src.utils.GetRadomNumbers import get_random_number

def Task1():
  print("#######################################")
  print("# For the pros and cons of using")
  print("# a linked list, see the README.md")
  print("#######################################")

  # Selects a random number between 3 and 20
  # Used as the amount of numbers to add to the linked list
  while True:
    amount_of_numbers = get_random_number(20)
    if amount_of_numbers > 3:
      break

  print("Number of elements to add:", amount_of_numbers)

  linked_list = LinkedList()
  
  for _ in range(amount_of_numbers):
    linked_list.append(get_random_number(100))
  
  print_linked_list(linked_list)

  print("Current linked list count:", linked_list.get_count())
  
  
def print_linked_list(linked_list):
  current = linked_list.head
  while current is not None:
    print("Current node value:", current.value, "Next node value:", current.nxt.value if current.nxt is not None else None)
    current = current.nxt
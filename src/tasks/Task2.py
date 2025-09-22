from src.utils.DoubleLinkedList.DoubleLinkedList import DoubleLinkedList
from src.utils.GetRadomNumbers import get_random_number

def Task2():
  ddl = DoubleLinkedList()
  ddl.add_first(10)
  ddl.add_first(20)
  
  ddl.add_last(5)
  
  print(ddl.head.value) # 20
  print(ddl.tail.value) # 10
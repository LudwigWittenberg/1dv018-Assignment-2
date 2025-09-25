from src.utils.HashTabelSeperateChaning.HTSC import HTSC
import random

def Task4():
  print("Task4: Testing with 5 different names")
  ht = HTSC()
  
  values = ["Ludwig", "Samuel", "Jonathan", "Benjamin", "Lucas"]
  
  for value in values:
    ht.insert(value)
    
  print("Hash Table Size:", len(ht))
  print()
  
  print("Task4: Testing with 200 random numbers")
  ht2 = HTSC()

  for index in range(200):
    value = random.randint(1, 100_000)
    ht2.insert(value)

  print("Hash Table Size:", len(ht2))
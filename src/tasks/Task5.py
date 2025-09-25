import random
from src.utils.Vehicle.Vehicle import Vehicle
from src.utils.HashTabelSeperateChaning.HTSC import HTSC

def Task5():
  random_int = random.randint(1000, 9999)
  vehicles = [Vehicle() for _ in range(random_int)]
  
  num_of_buckets = random_int // 5
  
  hash_table = HTSC(num_of_buckets)
  
  for v in vehicles:
    hash_table.insert(v)
    
  print(f"Number of vehicles: {len(vehicles)}")
  print(f"Number of buckets: {num_of_buckets}")
  print(f"Number of vehicles in hash table: {len(hash_table)}")
  print(f"Number of conflicts: {hash_table.count_conflicts()}")
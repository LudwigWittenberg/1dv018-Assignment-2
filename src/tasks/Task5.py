import random
from src.utils.Vehicle.Vehicle import Vehicle
from src.utils.HashTabelSeperateChaning.HTSC import HTSC

def Task5():
  random_int = random.randint(1000, 9999)
  print("Generating Vehicles...")
  vehicles = [Vehicle() for _ in range(random_int)]
  
  num_of_buckets = random_int // 5
  
  print("Creating hash table with,", num_of_buckets, "buckets")
  hash_table = HTSC(num_of_buckets)
  
  for v in vehicles:
    hash_table.insert(v)
    
  print(f"Number of vehicles: {len(vehicles)}")
  print(f"Number of vehicles in hash table: {len(hash_table)}")
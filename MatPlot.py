import random
from src.utils.Vehicle.Vehicle import Vehicle
from src.utils.HashTabelSeperateChaning.HTSC import HTSC
from collections import Counter
import matplotlib.pyplot as plt

def GenerateGraphs():
  random_int = random.randint(10_000, 100_000)
  vehicles = [Vehicle() for _ in range(random_int)]
  
  num_of_buckets = random_int // 5
  
  hash_table = HTSC(num_of_buckets)
  
  for v in vehicles:
    hash_table.insert(v)
    
  conflicts = hash_table.count_conflicts()  # This should be a list, one value per bucket

  conflict_counter = Counter(conflicts)

  # Prepare data for plotting
  x = sorted(conflict_counter.keys())  # unique conflict counts
  y = [conflict_count * conflict_counter[conflict_count] for conflict_count in x]  # total conflicts for each group

  plt.figure(figsize=(10, 6))
  plt.bar(x, y, color='skyblue', edgecolor='black', alpha=0.7)

  plt.title('Total Conflicts per Conflict Count', fontsize=18, fontweight='bold', loc='left', pad=20)
  plt.xlabel('Conflicts per Bucket', fontsize=14)
  plt.ylabel('Total Conflicts (all buckets with this count)', fontsize=14)
  plt.xticks(fontsize=12)
  plt.yticks(fontsize=12)

  plt.text(
      0.99, 0.98,
      f'Total vehicles: {len(vehicles)}\n Total buckets: {num_of_buckets}\n Hash table length: {len(hash_table)}',
      horizontalalignment='right',
      verticalalignment='top',
      transform=plt.gca().transAxes,
      fontsize=12,
      bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray')
  )

  plt.tight_layout()
  plt.savefig("graphs/hash_table_conflicts.png")
  
GenerateGraphs()

import random

def get_random_numbers(size):
  # Returnera hela intervallet från 0 till +size
  return list(range(0, size + 1))

def get_random_number(size):
  return random.randint(0, size)

def get_x_random_numbers(size, x):
  numbers = get_random_numbers(size)
  unique = list(set(numbers)) 
  random.shuffle(unique)
  print(unique)
  return unique[:x]
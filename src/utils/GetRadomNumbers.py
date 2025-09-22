import random

def get_random_numbers(size):
  # Returnera hela intervallet från -size till +size
  return list(range(-size, size + 1))

def get_random_number(size):
  return random.randint(0, size)
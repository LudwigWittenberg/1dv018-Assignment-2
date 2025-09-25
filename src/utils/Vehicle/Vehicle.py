import random

class Vehicle:
  def __init__(self):
    self.set_reg_number()
    
  def set_reg_number(self):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    self.reg_number = ""
    
    # Generate a random registration number in the format: "ABC12D"
    for _ in range(3):
      self.reg_number += random.choice(letters)
    for _ in range(2):
      self.reg_number += random.choice(digits)
    for _ in range(1):
      self.reg_number += random.choice(letters)
      
  def __hash__(self):
    hv = 17
    
    hv = 31 * hv + hash(self.reg_number)
    
    return hv
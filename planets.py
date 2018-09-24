#
# Name: Ryan Madamba
# Student ID: 014684341
# 9/24/18
# Lab 0
# Section 15
# Prompts user what their weight is and will RETURN their weight on Mars and Jupiter

def weight_on_planets():
   weight = int(input("What do you weigh on earth? "))
   mars = weight * 0.38
   jupiter = weight * 2.34
   print("\nOn Mars you would weigh", mars, "pounds.\n" + "On Jupiter you would weigh", jupiter, "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()

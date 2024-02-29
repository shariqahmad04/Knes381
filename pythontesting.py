from time import sleep
import os



n = os.get_terminal_size().lines
print(n)
print("\n" * (n-15)+ "rocket")


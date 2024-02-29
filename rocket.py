from time import sleep
import os

print("Start the countdown!!")

for second in range(10, 0, -1):
    print(second)
    sleep(1)
    
print("Lift off!")

sleep(1)
os.system("clear") #make everything above clear once the rocket launches



rocket = """
            
            
            
            
               -
              /  \\
              | - |
              |   |
            /       \\
           /         \\
          /           \\
          
           |          |
           |          |
           |          |
           |          |
           |          |
           |          |
            
            """


n_lines = os.get_terminal_size().lines

for l in range (1, n_lines, +1):
    os.system("clear")
    frame = "\n" * (n_lines - 14 - l) + rocket + "\n" * l
    print(frame)
    sleep(1 / l)





# delay = 300

''' for i in range(60):
       # print("\n")
        #sleep(delay/1000)
        #delay = delay * 0.9
    '''
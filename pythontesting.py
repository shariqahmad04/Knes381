from time import sleep
import os

print("Start the countdown!!")

''' for second in range(10, 0, -1):
    print(second)
    sleep(1)'''
    
print("Lift off!")

sleep(1)
os.system("clear") #make everything above clear once the rocket launches



def printRocket():
       print(
       """










       






                   //\\
                  ||##||
                 //##mm\\
                //##*mmm\\
               //###**mmm\\
              //###***nmmm\\
             //####***@nmmm\\
             ||####***@nnmm||
             ||####**@@@nnm||
             |______________|
             |    Krogg97   |
              \____________/
               |          |
              /|    /\    |\
             /_|    || /\ |_\
               |      NUSA|
               |       \/ |
               |          |
              /|    /\    |\
             / |    ||    | \
            /  |    ||    |  \
           /  /\    ||    /\  \
          |__/  \   ||   /  \__|
            /____\      /____\
            |    |      |    |
            |    |______|    |
            |    | /--\ |    |
            |____|/----\|____|
             \||/ //##\\ \||/
             /##\//####\\/##\
            //##\\/####\//##\\
           ||/::\||/##\||/::\||
           \\\''///:**:\\\''///
            \\\///\::::/\\\///
             \\//\\\::///\\//
              \/\\\\..////\/
                 \\\\////
                  \\\///
                   \\//
                    \/ """ )
       
printRocket()



delay = 300

for i in range(60):
    print("\n")
    sleep(delay/1000)
    delay = delay * 0.9

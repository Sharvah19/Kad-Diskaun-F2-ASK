'''
sharvah 11/6/2020

this code will do ...
exmpale ...

'''

from os import system
system('cls')  # to clear the screen


kad = input("Masukkan jenis kad diskaun anda:")
x=kad.casefold()
#print(x)

try:
    while True:
     if x == "kad premium":
        mata = int(input("Masukkan mata ganjaran kad anda:"))

        if(mata >= 500):
            print("Peratus diskaun ialah 50%")
        
        elif(mata >= 400):
            print("Peratus diskaun ialah 40%")

        elif(mata >= 300):
            print("Peratus diskaun ialah 30%")

        elif(mata >= 200):
            print("Peratus diskaun ialah 20%")

        elif (mata >= 100):
            print("Peratus diskaun ialah 10%")

        else:
            print("Maaf mata anda tidak mencukupi untuk mendapat diskaun")

     else:
        print("Maaf anda memerlukan kad premium untuk mendapat diskaun")
        break

except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	system('cls')	
	print('Bye!')

    
    

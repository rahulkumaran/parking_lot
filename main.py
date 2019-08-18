import sys
from parking_lot.parking import Cars

if(__name__=='__main__'):
    car = Cars()
    if (len(sys.argv)==2):
        file = open(sys.argv[1],'r+')
        for line in file:
            car.action(line.split(" "))

    elif(len(sys.argv)==1):
        command = ""
        while(True):
            command = input("\n$ ")
            car.action(command.split(" "))

    else:
        print("Please run the program in the right manner!")

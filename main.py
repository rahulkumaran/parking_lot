import sys
from parking_lot.parking import ParkingLot

if(__name__=='__main__'):
    parking = ParkingLot()
    if (len(sys.argv)==2):
        file = open(sys.argv[1],'r+')
        for line in file:
            parking.action(line.split(" "))

    elif(len(sys.argv)==1):
        command = ""
        while(True):
            command = input("\n$ ")
            parking.action(command.split(" "))

    else:
        print("Please run the program in the right manner!")

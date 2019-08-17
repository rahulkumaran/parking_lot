import sys

class ParkingLot:
    def __init__(self):
        self.slots = 0

    def create_parking_lot(self, slots):
        return slots

    def park(self, reg_no, colour):
        return reg_no

    def leave(self, slot):
        return slot

    def status(self):
        return 0

    def registration_numbers_for_cars_with_colour(self, colour):
        return statement

    def slot_numbers_for_cars_with_colour(self, colour):
        return statement

    def slot_number_for_registration_number(self, reg_no):
        return reg_no

    def action(self, command):
        if(command[0]=="create_parking_lot"):
            self.create_parking_lot(command[1])
        elif(command[0]=="park"):
            self.park(command[1], command[2])
        elif(command[0]=="leave"):
            self.leave(command[1])
        elif(command[0]=="status" or command[0]=="status\n"):
            self.status()
        elif(command[0]=="registration_numbers_for_cars_with_colour"):
            self.registration_numbers_for_cars_with_colour(command[1])
        elif(command[0]=="slot_numbers_for_cars_with_colour"):
            self.slot_numbers_for_cars_with_colour(command[1])
        elif(command[0]=="slot_number_for_registration_number"):
            self.slot_number_for_registration_number(command[1])
        elif(command[0]=="exit"):
            exit()
        else:
            print("Command not recognised!")
        return 1


if (len(sys.argv)==2):
    file = open(sys.argv[1],'r+')
    parking = ParkingLot()
    for line in file:
        #print(line)
        parking.action(line.split(" "))
elif(len(sys.argv)==1):
    command = ""
    parking = ParkingLot()
    while(True):
        command = input("\n$ ")
        command = command.split(" ")
        parking.action(command)
else:
    print("Please run the program in the right manner!")

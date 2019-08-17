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


if (len(sys.argv)==2):
    file = open(sys.argv[1],'r+')
    parking = ParkingLot()

elif(len(sys.argv)==1):
    command = ""
    parking = ParkingLot()
    while(True):
        command = input("\n$ ")
        command = command.split(" ")
else:
    print("Please run the program in the right manner!")

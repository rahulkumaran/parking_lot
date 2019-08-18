import sys

class ParkingLot:
    def __init__(self):
        self.slots = -1
        self.blocked = []
        self.occupancy = []

    def create_parking_lot(self, slots):
        '''
        Class function to help create
        the parking lot with required
        slots

        slots : string
        '''
        try:
            if(int(slots) < 0):
                print("Cannot create parking with negative slots")

            elif('\n' in str(slots)):
                print("Created a parking lot with " + str(slots[0:-1]) + " slots")
            else:
                print("Created a parking lot with " + str(slots[0]) + " slots")
            self.slots = int(slots)
            return slots
        except ValueError:
            print("Please enter an integer number of slots!")
            return 0

    def status(self):
        '''
        Class function to check status
        of the car parking at any given
        period.

        '''
        if(len(self.blocked)==0):
            print("No cars found in parking lot at the moment.")
        print("Slot No.\tRegistration No\t\tColour")
        cars = self.occupancy
        for details in cars:
            print(str(details[0]) + '\t\t' + details[1] + '\t\t' + details[2])
        return self.blocked

    def registration_numbers_for_cars_with_colour(self, colour):
        '''
        Class function to get the
        registration number of cars
        given the colour.

        colour : string
        '''
        try:
            cars = self.occupancy
            statement = ""
            for details in cars:
                if(colour in details):
                    statement += details[1] + ", "
            if(statement == ""):
                print("No cars found in the parking lot with the colour " + colour)
            else:
                print(statement[0:-2])
            return statement[0:-2]
        except:
            print("Sorry, faced an unexpected trouble. Please type in your command again!")
            return 0

    def slot_numbers_for_cars_with_colour(self, colour):
        '''
        Class function to retrieve
        slots of cars in parking lot
        given a colour

        colour : string
        '''
        try:
            cars = self.occupancy
            statement = ""
            for details in cars:
                if(colour in details):
                    statement += str(details[0]) + ", "
            if(statement == ""):
                print("No cars found in the parking lot with the colour " + colour)
            else:
                print(statement[0:-2])
            return statement[0:-2]
        except:
            print("Sorry, faced an unexpected trouble. Please type in your command again!")
            return 0

    def slot_number_for_registration_number(self, reg_no):
        '''
        Class function to retrieve
        slot of car in parking lot
        given registration number.

        reg_no : string
        '''
        try:
            cars = self.occupancy
            iter = 1
            if('\n' in reg_no):
                reg_no = reg_no[0:-1]
            for details in cars:
                if(reg_no in details):
                    print(str(details[0]))
                    break
                iter += 1
            if(iter-1 == self.slots):
                print("Not Found")
            return details[0]
        except:
            print("Sorry, faced an unexpected trouble. Please type in your command again!")
            return 0

class Cars(ParkingLot):
    def __init__(self):
        super().__init__()

    def park(self, reg_no, colour):
        '''
        Class function to park cars
        in the parking

        reg_no : string
        colour : string
        '''
        try:
            if(self.slots == -1):
                print("Please create a parking lot first to park cars!")
            elif(len(self.blocked)==self.slots):
                print("Sorry, parking lot is full")
                return 0
            else:
                all_slots = [x for x in range(1, self.slots + 1)]
                block_list = set(self.blocked)
                available = list(block_list ^ set(all_slots))
                self.blocked += [available[0]]
                self.occupancy += [[available[0], reg_no, colour]]
                print("Allocated slot number: " + str(available[0]))
            return reg_no
        except:
            print("Sorry, faced an unexpected trouble. Please type in your command again!")
            return -1

    def leave(self, slot):
        '''
        Class function to release
        parking slots from parking
        lot when they leaveself.

        slot : string
        '''
        try:
            position = 0
            for car in self.occupancy:
                if(int(slot) in car):
                    del self.occupancy[position]
                    del self.blocked[position]
                    break
                position += 1
            if('\n' in str(slot)):
                print("Slot number " + str(slot[0:-1]) + " is free")
            else:
                print("Slot number " + str(slot) + " is free")
            return slot
        except ValueError:
            print("Please enter an integer number of slots!")
            return -1

    def action(self, command):
        '''
        Class function to help redirect
        code to required function after
        parsing commands

        command : string
        '''
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

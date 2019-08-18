# Parking Lot

The folder consists of the files required to make this program run. The base structure is kept as it is.<br><br>

New files that have been added are :<br>
1) main.py --> Consists code for parsing and sending commands to main class<br>
2) parking/ --> Folder consists of parking.py that has 2 classes ParkingLot and Cars with the required functions.<br>
3) test.py --> Consists of code for testing this program<br><br>

The files that were edited were : <br>
1) bin/setup --> Commands to run the tests and compile the necessary python files are placed here.<br>
2) bin/parking_lot --> Commands to run the python script is placed here.<br><br>

The assumptions made were :<br>
1) The input file will always be kept in the base folder or in a folder inside the base folder.<br><br>

The program gives the required output and also, some additional features mentioned below were added.<br>
1) Incase the command is not recognised by program, it says `Command not recognised!` but keeps the terminal running<br>
2) An error message is placed incase inputs aren't of the right format. For example, if while creating a parking lot, someone passes `abc` as an argument for number of slots, the error message is sprung up by the program but the program won't quit.<br>
3) An actions function has been added to the class to ensure that the command is parsed and sent to the right functions to perform as required.<br>
4) In the interactive terminal mode of this program, the program goes on until you type `exit` whereas in the file input mechanism, the program runs until end of file and quits provided exit is not given anywhere in the list of commands in the file.<br>
5) Exception handling has been done for most functions.<br>

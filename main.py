import sys
from parking_lot.parking import Cars

if(__name__=='__main__'):
	car = Cars()
	if (".txt" in sys.argv[1]):
		sys.argv[1] = sys.argv[1].replace('\n',"")
		file = open(sys.argv[1],'r+')
		for line in file:
			car.action(line.split(" "))

	else:
		command = ""
		while(True):
			command = input("\n$ ")
			car.action(command.split(" "))


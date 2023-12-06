import sys

def insert(array, pos, stype, sequence):
    pass

def printAll(array):
    pass

def printPos(array, pos):
    pass

def copy(array, pos1, pos2):
    pass

def swap(array, pos1, start1, pos2, start2):
    pass

def complement(sequence):
    pass

def transcribe(array, pos):
    pass

def remove(array, pos):
    pass

argCount = len(sys.argv)
args = sys.argv

commandFileName = None
arraySize = 100

if argCount == 2:
    commandFileName = args[1]
elif len(sys.argv) == 3:
    arraySize = int(args[1])
    commandFileName = args[2]
else:
    print("This program should be invoked from the command-line as:")
    print("python3 bio.py <command-file>")
    print("or")
    print("python3 bio.py <array size> <command-file>")

sequenceArray = tuple([None, None] for i in range(arraySize))

lines = None

try:
    ifile = open(commandFileName, "r")
    lines = ifile.readlines()
    ifile.close()

except IOError:
    print("file not found")
    exit(1)

for line in lines:
    command = line.split()[0]

    if command == "insert":
        print('do something')
    elif command == "print":
        print('do something')
    elif command == "copy":
        print('do something')
    elif command == "swap":
        print('do something')
    elif command == "transcribe":
        print('do something')
    elif command == "remove":
        print('do something')
    else:
        print(command)
        print("unknown command")

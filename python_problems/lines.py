import sys

size = len(sys.argv) 
if size < 2:
    sys.exit("Too few command-line arguments")

if size > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")    

count = 0
for line in file:
    if not line.strip().startswith("#") and line.strip() != "":
        count += 1
file.close()
print(count)        



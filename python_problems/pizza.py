import sys,csv
from tabulate import tabulate
size = len(sys.argv) 
if size < 2:
    sys.exit("Too few command-line arguments")

if size > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit("File does not exist")    

items = []
g_list = csv.reader(file)

for li in g_list:
    items.append(li)

file.close()
print(tabulate(items,headers="firstrow",tablefmt="grid"))   

import sys,csv
size = len(sys.argv) 
if size < 3:
    sys.exit("Too few command-line arguments")

if size > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    before = open(sys.argv[1])
    
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}") 

persons = []
r = csv.reader(before)
next(r)

for l in r:
    fi,la = l[0].split(",")
    persons.append([fi,la.strip(),l[1]])

before.close()

with open(sys.argv[2],"w",newline="") as after:
    w = csv.writer(after)
    w.writerow(["first","last","house"])
    for l in persons:
        w.writerow(l)


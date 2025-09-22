import sys
from PIL import Image,ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

extensions = (".jpg",".png",".jpeg")
if not sys.argv[1].endswith(extensions): 
    sys.exit("Invalid Input") 

if not sys.argv[2].endswith(extensions):
    sys.exit("Invalid output")
for item in extensions:
    if sys.argv[1].endswith(item) and sys.argv[2].endswith(item):
        break
else:
    sys.exit("Input and output have different extensions")

try:
    img = Image.open(sys.argv[1])

except:
    sys.exit("Input does not exist")

shirt = Image.open("instances/shirt.png")
size = shirt.size
img = ImageOps.fit(image = img,size=size)
shirt = Image.open("instances/shirt.png")
img.paste(shirt,shirt) # = (shirt,(0,0),mask= shirt)
img.save(sys.argv[2])




#figlet short for Frank, Ian and Glen’s Letters

import sys
import random
from pyfiglet import Figlet
size = len(sys.argv)
f = Figlet()
f_list = f.getFonts()
font_u = ""
if size > 3 or size == 2:
    sys.exit("Invalid usage")

elif size == 3:
    font_u = sys.argv[2] 
    if not sys.argv[1] in ["-f","--font"] or not font_u in f_list:  
        sys.exit("Invalid usage")
       
text = input("Input: ")
if font_u != "":
    f.setFont(font = font_u )
else:
    f.setFont(font = random.choice(f_list))

print(f.renderText(text))          




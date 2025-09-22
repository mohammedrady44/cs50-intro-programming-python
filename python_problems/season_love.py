import re
from datetime import date ,datetime
import sys
import inflect
   
def main():
   print(get())


def check(dat):
   d = re.search(r"^(\d{4})-(\d{2})-(\d{2})$",dat)
   if d:
       
      y,m,e = int(d.group(1)),int(d.group(2)),int(d.group(3))
      try:
         date(y,m,e)
      except:
          sys.exit("invalid date")
      return y,m,e                             
   else:
     sys.exit("invalid date")  
 

def get():
   d = input("Datetime: ")
   y,m,e = check(d)
   now = date.today()
   d1 = datetime(y,m,e)
   d2 = datetime(2000,1,1)
   s = d2-d1
   r =  s.days*24*60
   q = inflect.engine()
   return  q.number_to_words(r,andword="")+" "+"minutes"
   





if __name__ == "__main__":
   main()

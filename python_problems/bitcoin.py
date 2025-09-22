import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit("too many command-line arguments")

try:
    num = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")    

try:
    o = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()
except:
    sys.exit("error")

amount = o["bpi"]["USD"]["rate_float"] * num
print(f"${amount:,.4f}")

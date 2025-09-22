months= [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        my_date = input("Date: ").split("/")
        if len(my_date) == 1:
            mon_day,year = my_date[0].split(",")
            my_date = mon_day.split(" ")
            my_date[0] = my_date[0].lower().capitalize()
            for i in range(0,len(months)):
                if months[i] == my_date[0]:
                    break
            else:
                continue
            my_date[0] = i+1
            my_date.append(year.strip())
                
        month,day,year = int(my_date[0]),int(my_date[1]),int(my_date[2])    
        if  not (month >= 1 and month <= 12) or not (day >= 1 and day <= 31):
            continue
        break
    except:
        pass

print(f"{year}-{month:02}-{day:02}")


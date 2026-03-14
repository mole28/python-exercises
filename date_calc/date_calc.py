import calendar

print("A program to test that given a date in the last century (from 1926 to 2026)")
print("we will return what day of the week it was.")
the_date = input("Enter a date (DD/MM/YYYY or DD/MM/YY):\n")

parts = the_date.split("/")
day = int(parts[0])
month = int(parts[1])
year = int(parts[2])

# Another way, you can do Without using split, this is how it could be done
#day = int(the_date[:2])    
#month = int(the_date[3:5])
#year = int(the_date[6:])

if year < 100:
    if year > 26:
        year+= 1900
    else:
        year+=2000

if 1926 <= year <= 2026:
    day_num = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_num]
    print("the date: " + str(day) + "/" + str(month) + "/" + str(year) + " was in " + 
        str(day_name))
else:
    print("Error: The year " + str(year) + " is out of the supported range (1926-2026).")
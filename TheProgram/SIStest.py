from datetime import datetime
datetime_object = "01/12/2020"
current_date = datetime.today()
mydate = datetime.strptime(datetime_object,'%d/%m/%Y')
mydate2 = datetime.strftime(current_date,'%d/%m/%Y')
print(current_date)
print(mydate)
print((current_date-mydate).days)

if current_date < mydate:
    print("datetime1 is Greater")
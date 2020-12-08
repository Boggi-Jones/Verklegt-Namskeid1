from datetime import datetime
date = "08/12/2020"
current_date = datetime.today()
return_date = datetime.strptime(date + " 23:59", '%d/%m/%Y %H:%M')
print(return_date)
current_date2 = datetime.strftime(current_date,'%d/%m/%Y')
print(current_date)

if current_date > return_date:
    print("fokk")
import datetime

print("Bugün:",datetime.date.today())
print("Şimdi =", datetime.datetime.now())
simdi=datetime.datetime.now()
print(simdi.strftime("%d/%m/%Y %H:%M:%S"))
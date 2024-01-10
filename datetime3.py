import time
import datetime

while True:

 #   clear = lambda: os.system('cls')
 #   clear()

    simdi=datetime.datetime.now()
    print(simdi.strftime("%H:%M:%S"))
    time.sleep(1)
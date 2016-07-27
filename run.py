# https://github.com/dbader/schedule/blob/master/FAQ.rst
import helper, schedule, time
import helper.email as email

'''
# Created by Paul Cameron
# This script was created to transfer files from Win7 to remote machine
'''
d = ''
print("This task manager will pull a SL config file")

if d == ():
    helper.main_station()

else:
    schedule.every().wednesday.at("14:30").do(helper.main_station)
    print("\nWaiting till Wed @ 2:30")
    while True:
        schedule.run_pending()
        time.sleep(1)

#  email.conn() McAfee is blocking the required ports


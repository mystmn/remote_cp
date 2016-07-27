# https://github.com/dbader/schedule/blob/master/FAQ.rst
import helper, schedule, time
import helper.email as email

'''
# Created by Paul Cameron
# This script was created to transfer files from Win7 to remote machine
'''
d = ''

if d == ():
    helper.main_station()
else:
    schedule.every().wednesday.at("09:00").do(helper.main_station)

    while True:
        schedule.run_pending()
        time.sleep(1)

#  email.conn() McAfee is blocking the required ports


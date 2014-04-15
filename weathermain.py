import slugTools
import time
import re
from ftplib import FTP

awUser = 'NJCHE'
awPass = 'NJCHE'
awFilename = 'COUW' + slugTools.slugTomorrowString() + '.pdf' 

print "filename " + awFilename
print "\n"

time.sleep(1)

print "filename " + awFilename
print "\n"

quit()

AW = ftplib.FTP()

AW.connect('FTP.ACCUWEATHER.COM')
AW.login(awUser,awPass)

AW.retrbinary(awFilename, callback=None)




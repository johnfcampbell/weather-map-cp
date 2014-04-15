import slugTools
import flatConfig
import time
import re
from ftplib import FTP

awFilename = 'COUW' + slugTools.slugTomorrowString() + '.pdf'

print "Weather filename " + awFilename
print "\n"

time.sleep(1)

accu = flatConfig.getConfig('weather.cfg')
awUser = accu['user']
awPass = accu['pass']
awServer = accu['server']


# create an FTP object, connect and log in.
AW = FTP()

print "created FTP object\n"

AW.connect(awServer)
AW.login(awUser,awPass)


awGet = 'RETR ' + awFilename

with open(awFilename,'wb') as pdf:
    AW.retrbinary(awGet, pdf.write)


AW.quit()
#quit()

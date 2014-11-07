# author: Jose R de la Vega
# email : j.r.delavega17@gmail.com

from json import dumps, loads
from urllib2 import urlopen, Request
import datetime

# this is my token, a dictionary that has the key(token) and value(... the tokens value)
info = {'token':'haTzzCr65h'}

# now lets POST out token(using Request)
req = Request('http://challenge.code2040.org/api/time', data=dumps(info))

# lets get the dictionary out of what we recieved
rec = loads(urlopen(req).read())['result']

# now lets get a variable for each value of the 
# dictionary

datestamp = rec['datestamp']
interval = rec['interval']

# I'll print the datestamp and the interval

print 'Datestamp: ' + datestamp
print 'Interval: ' + str(interval)

# since we already know in which format the
# datestamp is given(ISO 8601), we can define
# the different parts of the datestamp

year = datestamp[:4]
month = datestamp[5:7]
day = datestamp[8:10]
hour = datestamp[11:13]
minute = datestamp[14:16]
second = datestamp[17:19]
microsecond = datestamp[20:23]

# so that is that.. just splitting the datestamp
# and now we have all the data separated! I will
# use the separated data to make a datetime object

time = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond))

# now i can use a daytime function called timedelta
# that will help me add the interval to the datetime
# object created in line 44(time)

newTime = time + datetime.timedelta(seconds=interval)

# datetime has a function called isoformat() that 
# returns a string representing the date in ISO 8601 format

resTime = newTime.isoformat()

# let's print the result time(restime)
print 'Result time: ' + resTime

# now create the final dictionary
send = {'token':'haTzzCr65h', 'datestamp':resTime}

# now make a Request with the dictionary... 
res = Request('http://challenge.code2040.org/api/validatetime',data=dumps(send))

# now res has a JSON and we already know hot to get the string from this
final = loads(urlopen(res).read())['result']

# finally lets print the final variable and check if we passed the stage 2
print final
# author: Jose R de la Vega
# email : j.r.delavega17@gmail.com

from json import dumps, loads
from urllib2 import urlopen, Request

# this is my token, a dictionary that has the key(token) and value(... the tokens value)
info = {'token':'haTzzCr65h'}

# now lets POST out token(using Request)
req = Request('http://challenge.code2040.org/api/prefix', data=dumps(info))

# lets get the dictionary out of what we recieved
rec = loads(urlopen(req).read())['result']

# now I'll create a prefix variable to hold the vaule
# of the prefix and a array to hold the array value

prefix = rec['prefix']
array = rec['array']

# now I'll print the array and the prefix
print 'Prefix: ' + prefix
print 'Array:', array

# I will create new array that will hold the strings
# that dont have the prefix

resArray = []

# now I'll go through the array to find and copy the
# strings without the prefix to the resArray. I'll do that by
# checking if the first n characters of the string
# are not equal to the prefix, where n is the length of 
# the prefix. That is done with len(prefix), and with
# the e[:x] i get the first x characters of e! NICE


for e in array:
	if e[:len(prefix)] != prefix:
		resArray.append(e)

# let's print the new array(resArray)
print 'New array: ', resArray

# now create the final dictionary
send = {'token':'haTzzCr65h', 'array':resArray}

# now make a Request with the dictionary... 
res = Request('http://challenge.code2040.org/api/validateprefix',data=dumps(send))

# now res has a JSON and we already know hot to get the string from this
final = loads(urlopen(res).read())['result']

# finally lets print the final variable and check if we passed the stage 2
print final
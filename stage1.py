# author: Jose R de la Vega
# email : j.r.delavega17@gmail.com

from json import dumps, loads
from urllib2 import urlopen, Request

# this is my token, a dictionary that has the key(token) and value(... the tokens value)
info = {'token':'haTzzCr65h'}

# I use dumps to encode my dictionary called info to JSON... kind of obvious comment...
# if you read the docs :D
token = dumps(info)

# req will have the JSON that haves the string i need to reverse
req = Request('http://challenge.code2040.org/api/getstring', token)

# Ok so this can be a little ugly, but it's not that hard to get...
# So basically urlopen will open the Request made in line 15, then 
# read will read the Request(you don't say!), once you have read the
# Request youll have a JSON which you will have to decode using loads()
# and now you'll have a dictionary with the key(result) and value
# (the string to be reversed) and we assign the value to the variable
# text.

string = loads(urlopen(req).read())['result']

# I'll print the string just for fun :)

print "This is the string: " + string

# now that we have the string we can create a variable to hold the 
# reversed string... I'll call it gnirts(see what I did there?)

gnirts = string[::-1]

# now lets print gnirts

print "This is the reversed string: " + gnirts

# now we have to create a new dictionary to contain two pairs of key/value
# first will have my info(line 8) and the other will be key(string) and
# value(gnirts)

send = {'token':'haTzzCr65h', 'string':gnirts}

# now make a Request with the dictionary... note that this time I encoded the
# dictionary inside of the Request... economizing lines

res = Request('http://challenge.code2040.org/api/validatestring', data=dumps(send)) 

# now result has a JSON and we already know hot to get the string from this

final = loads(urlopen(res).read())['result']

# finally lets print the final variable and check if we passed the stage 1

print final
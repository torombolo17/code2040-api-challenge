# author: Jose R de la Vega
# email : j.r.delavega17@gmail.com
# notes : I will skip the large blocks of comments that I had in stage 1
#         to make the program faster and so that you dont get bored reading all that,
#         any doubts on how something works check the docs of the libraries or check if I
#         have a comment on that in stage1.py


from json import dumps, loads
from urllib2 import urlopen, Request

# this is my token, a dictionary that has the key(token) and value(... the tokens value)
info = {'token':'haTzzCr65h'}

# now lets POST out token(using Request)
req = Request('http://challenge.code2040.org/api/haystack', data=dumps(info))

# lets get the dictionary out of what we recieved
rec = loads(urlopen(req).read())['result']

# I'll print rec so that you can see the data that we got...
# it is a dictionary!!! :D

print rec

# now that we have a dictionary and we know that we will have 
# two values(needle and haystack), so we create the haystack
# and the needle to search that value in the list haystack

needle = rec['needle']
haystack = rec['haystack']

# now we get the index of needle in the list haystack using
# index(obj) which returns the first index containing obj
# in a list and since the value of needle will appear once
# in the haystack... TADAAAAA we will get the index.

pos = haystack.index(needle)

# I'll print the position of the needle so that you can confirm
# it by looking on the previously printed dictionary

print 'Needle is in position ' + str(pos)

# now create the final dictionary
send = {'token':'haTzzCr65h', 'needle':pos}

# now make a Request with the dictionary... 
res = Request('http://challenge.code2040.org/api/validateneedle',data=dumps(send))

# now res has a JSON and we already know hot to get the string from this
final = loads(urlopen(res).read())['result']

# finally lets print the final variable and check if we passed the stage 2
print final
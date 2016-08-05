'''Find Interfaces in an IOS config'''

from ciscoconfparse import CiscoConfParse

parse = CiscoConfParse('rtr-config.txt', syntax='ios')

all_intfs = parse.find_objects(r"^interf")

ip_addr = list()
for obj in all_intfs:
	ip = parse.find_objects(r'^ip')
	ip_addr.append(ip)

print 'Interface is: %s' % obj.text
print "IP address is: ", ip_addr


'''ip_addr = list()

for obj in all_intfs:
	ip = obj.re_search_children(r"^ip\saddress*")
	ip_addr.append(ip)
	print ip_addr'''

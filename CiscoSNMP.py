#Code adds a new SNMP RO community string

import pexpect
import sys
import os

# Creates Variables to be referenced by code
router_usrn = "cisco"
router_pwd = "cisco"
enable_pwd = "cisco"

# Creat a logfile
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

# Import flat file of Router IP's and Login

with open('devices.txt') as filename:
    routers = filename.read().splitlines()
for router in routers:
	print router
	task = pexpect.spawn('telnet %s@%s' % (router_usrn, router))
	# Drop logfile to Standard Out.
	task.logfile = sys.stdout
	task.expect('Password:')
	task.sendline(router_pwd)
	task.expect('>')
	task.sendline('terminal length 0')
	task.expect('\>')
	task.sendline('enable')
	task.expect('Password:')
	task.sendline(enable_pwd)
	task.expect('#')
	task.sendline('conf t')
	
	# This section starts the configuration of SNMP 
	task.expect('\(config\)#')
	task.sendline('snmp-server community TEST ro')
	task.expect('\(config\)#')
	task.sendline('exit')
	task.expect('#')
	
	#terminate the session
	task.sendline('end')
	task.expect('#')
	task.sendline('wr mem')
	task.expect('#')
	task.sendline('quit')
	task.close()
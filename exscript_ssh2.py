'''This script logins into Cisco IOS devices via SSH to send configuration commands.
The script prompts for credentials and the flat file hosts.txt has the list of IP's to SSH.'''

import hashlib

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
import Exscript.protocols
from Exscript import Account
from Exscript.util.start import start
from Exscript.util.file import get_hosts_from_file

#prompts for crednetials
account = read_login()

#hosts.txt file has the list of IP Addresses
hosts = get_hosts_from_file('hosts.txt')
conn = SSH2()

def modified(job, host, conn):
	conn.send('enable\r')
	conn.auto_app_authorize(account)
	conn.execute('conf t')
	#add ios configuration commands below using the conn.execute command
	conn.execute('access-list 2 permit host 9.0.0.16')

log=open('log.txt','w+') #log output file
logerr=open('logerr.txt','w+') #log error output file

start(account, hosts, modified, stdout=log, stderr=logerr)

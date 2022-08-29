import os
import sys

try: # input command flag
    comflag = sys.argv[1]
except IndexError:
    print ('NO-command flag!')

try: # input domen files
    ddirin = sys.argv[2]
except IndexError:
    print ('NO-input file! - EXAMPLE sudo python3 dipdigban2.py -a file-domen-IN file-rezult-OUT')

try: # out domen files REZULT
    ddirout = sys.argv[3]
except IndexError:
    print ('NO-out file! --- EXAMPLE sudo python3 dipdigban2.py -a file-domen-IN file-rezult-OUT')

# EXAMPLE sudo python3 dipdigban2.py -a file-domen-IN file-rezult-OUT
data =[]

def reader(ddira):
    handle = open(ddira, "r")
    data = handle.readlines() # read ALL the lines!
    handle.close()
    return data

def testdomen(ddirout, data):
    file = open(ddirout, "w")
    for ip in data:
        flag = os.system ('ping -c 1 %s' % (ip))
        if flag == 0:
            print ('=================================')
            print (ip)
            print ('---------------------------------')
            file.write (ip)
            flag = 1
        else:
            pass

    file.close()

#flagurpl = '1' domen and ip, 2 - only ip
#printa = 1 - print ip and domen, all - only ip
def exploreip (ddirout, flagurpl, printa, data):
    file = open(ddirout, "w")
    for ip in data:
        flag = os.popen('dig +short %s' % (ip)).read()
        if printa == 1:
            print (ip, flag)
        else:
            pass

        s = '\n'
        if flagurpl == '1':
            flag = ip + flag + s
        else:
            flag = flag
        file.write (flag)

    file.close()

    if printa != 1:
        print ('- OK -')
    else:
        pass

def dablchek(ddirout, data):
    print(data)
    cleardabl = set(data)
    data = list(cleardabl)
    print('--- clear dabl dabl ---')
    print(data)
    file = open(ddirout, "w")
    for ip in data:
        flag = os.system ('sudo iptables -n -L -v --line-numbers | grep %s' % (ip))
        if flag != 0:
            print ('- write -')
            print (ip)
            file.write (ip)
            flag = 1
        else:
            print (' - dabl - ')
            print (ip)
    file.close()
    print('- Dabl chek OK - file:', ddirout)

def comgen(ddirout, datalocal):
    ddiroutcomm = '%s-command' % (ddirout)
    file = open(ddiroutcomm, "w")
    tabler = '\n'
    file.write ('#!/bin/bash\n')
    for ip in datalocal:
        ip = ip.replace('\n','')
        stringo1 = 'sudo iptables -t filter -A INPUT -s %s/32 -j REJECT' % (ip)
        stringo2 = 'sudo iptables -A FORWARD -s %s -j REJECT' % (ip)
        allstr = stringo1 + tabler + stringo2 + tabler
        file.write (allstr)
    file.close()
    os.system ('sudo chmod u+x %s' % (ddiroutcomm))
    print('- Command generation OK - file:', ddiroutcomm)


try:
    if comflag == '-a':
        data = reader(ddirin)
        print (data)
        testdomen(ddirout, data)
        print ('--- exploer ip ---')
        data = reader(ddirout)
        print(data)
        ddirout = '%s-dig' % (ddirout)
        exploreip (ddirout, '1', 1, data)
        ddiroutip = '%s-ip' % (ddirout)
        exploreip (ddiroutip, '2', 0, data)
        data = reader(ddiroutip)
        ddiroutipndbl = '%s-ndbl' % (ddiroutip)
        dablchek(ddiroutipndbl, data)
        data = reader(ddiroutipndbl)
        comgen(ddiroutipndbl, data)
        print ('- domen ip file:', ddirout)
        print ('- only ip file:', ddiroutip)
    elif comflag =='-t':
        data = reader(ddirin)
        print (data)
        testdomen(ddirout, data)
        print ('- testdomen OK - out file:', ddirout)
    elif comflag =='-e':
        data = reader(ddirin)
        print (data)
        ddirout = '%s-dig' % (ddirout)
        exploreip (ddirout, '1', 1, data)
        ddiroutip = '%s-ip' % (ddirout)
        exploreip (ddiroutip, '2', 0, data)
        print ('- explore ip OK - out file domen and IP:', ddirout)
        print ('- out file only IP:', ddiroutip)
    elif comflag =='-d':
        data = reader(ddirin)
        print(data)
        ddiroutipndbl = '%s-ndbl' % (ddirout)
        dablchek(ddiroutipndbl, data)
    elif comflag =='-c':
        data = reader(ddirin)
        comgen(ddirout, data)
    elif comflag =='-ta':
        data = reader(ddirin)
        print (data)
        testdomen(ddirout, data)
        saveddir = ddirout
        print ('--- exploer ip ---')
        data = reader(ddirout)
        print(data)
        ddirout = '%s-dig' % (ddirout)
        exploreip (ddirout, '1', 1, data)
        ddiroutip = '%s-ip' % (ddirout)
        exploreip (ddiroutip, '2', 0, data)
        print ('- testdomen OK - out file:', saveddir)
        print ('- explore ip OK - out file domen and IP:', ddirout)
        print ('- out file only IP:', ddiroutip)
    elif comflag =='-dc':
        data = reader(ddirin)
        ddiroutipndbl = '%s-ndbl' % (ddirout)
        dablchek(ddiroutipndbl, data)
        data = reader(ddiroutipndbl)
        comgen(ddiroutipndbl, data)
    else:
        print ('''- man flage - 
        -a [start all file :input file domen]
        -t [start test domen :input file domen]
        -e [start explore ip :input file domen]
        -d [start dabl check :input file IP]
        -c [start command generator :input file IP]
        -ta [start test domen and explore ip :input file domen]
        -dc [start dabl check and command generator :input file IP]
        EXAMPLE sudo python3 dipdigban2.py -[xx] file-INPUT file-rezult-OUT''')
except NameError:
    pass
except FileNotFoundError:
    print('INPUT FILE - not detected')
#!/usr/bin/python
import validators
import re
import httplib,urllib
import os,time
import requests

#Function to check valid domains based on Response Codes
def is_live(host, path="/"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("GET", path)
        return conn.getresponse().status
    except StandardError:
        return None

cwd = os.getcwd()
#For Nice Colors Stuff
ICyan="\033[0;96m"
IPurple="\033[0;95m"
IGreen="\033[0;92m"
IRed="\033[0;91m"
IWhite="\033[0;97m"

print '''\n%sCollects Subdomains from %s crt.sh %s\n
            >(%s:%sinit 6%s:%s)<\n
               /    \\\n
                |  |\n
              MrR3boot\n'''%(ICyan,IGreen,ICyan,IWhite,IRed,IWhite,ICyan)

#Reading input from user
domain = raw_input( "\nGive me a domain to start with: ")

#Domain Validation
validate = validators.domain(domain)

if validate:
        page = urllib.urlopen('https://crt.sh?q=%25.'+domain).read()
        domains = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)'+domain, page)
        uniqdom = set(domains)
        count = len(uniqdom)
        print '''%s\nFound %s Unique Subdomains :)\n'''%(IRed, count)
        print '''%s1. %sPrint Results'''%(ICyan,IWhite)
        print '''%s2. %sSave Results to output.txt'''%(ICyan,IWhite)
        print '''%s3. %sFind valid domains among Results\n'''%(ICyan,IWhite)
        choice = input('\033[0;92mEnter your choice\033[0;97m :')
        choice = int(choice)
        arraydom = []
        for valid in uniqdom:
                arraydom.append(valid)
        if choice == 1:
                for valid in uniqdom:
                        print valid
        elif choice == 2:
                with open(os.path.join(cwd, 'output.txt'), 'w') as file:
                        for valid in uniqdom:
                                file.write(valid + "\n")
                        print '''\n%sSuccessfully saved.'''%(ICyan)
        elif choice == 3:
                print "%sList of valid domains\n%s "%(IPurple,IWhite)
                for array in arraydom:
                        if str(is_live(array)) != "None":
                                code = str(is_live(array))
                                print array

else:
        print '''%sDo you think this is a valid Domain to look for ?'''%(IRed)

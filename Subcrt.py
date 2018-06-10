#!/usr/bin/python
import validators
import re
import urllib
import os

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
              MrR3boot'''%(ICyan,IGreen,ICyan,IWhite,IRed,IWhite,ICyan)

#Reading input from user
domain = raw_input( "\nGive me a domain to start with: ")

#Domain Validation
validate = validators.domain(domain)

if validate:
        page = urllib.urlopen('https://crt.sh?q=%25.'+domain).read()
        domains = re.findall(r'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)'+domain, page)
        uniqdom = set(domains)
	count = len(uniqdom)
	print '''%sFound %s Unique Subdomains :)'''%(IRed, count)
        print '''%sYou want me to print the results or do you want to save it for later usage ?'''%(IPurple)
        print '''%s1. %sPrint'''%(ICyan,IWhite)
        print '''%s2. %sSave to output.txt'''%(ICyan,IWhite)
        choice = input('\033[0;92mEnter your choice [1 or 2]\033[0;97m : ')
        choice = int(choice)
        if choice == 1:
                for valid in uniqdom:
                        print valid
        else:
                with open(os.path.join(cwd, 'output.txt'), 'w') as file:
                        for valid in uniqdom:
                                file.write(valid + "\n")
			print '''\n%sSuccessfully saved.'''%(ICyan)
else:
        print '''Do you think this is a valid Domain to look for ?'''


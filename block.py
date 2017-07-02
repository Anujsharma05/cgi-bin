#!/usr/bin/python
import cgi,os,commands,sys

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
name=data.getvalue('d_name')
size=data.getvalue('size')
print name
print size

#entry="sudo echo '/mnt/{} *(rw,no_root_squash)' >>/root/Desktop/new.txt".format(name)


"""
entry="sudo echo '/mnt/{} *(rw,no_root_squash)' >>/var/www/html/anuj.sh".format(name)
print entry
z=commands.getstatusoutput(entry)
print z
"""

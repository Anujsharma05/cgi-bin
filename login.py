#!/usr/bin/python
import cgi,os

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
uname=data.getvalue('uname')
passwd=data.getvalue('pass')

if uname=="test" and passwd=="123":
	print "<META HTTP-EQUIV='refresh' content='0; url=/cloud.html'/>"
else:
	print "Please check your username or password"

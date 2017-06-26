#!/usr/bin/python
import cgi,os

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
output=data.getvalue('cloud')
if output=="saas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/saas.html' target='_blank'/>"

if output=="staas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/staas.html' target='_blank'/>"

if output=="iaas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/iaas.html' target='_blank'/>"

if output=="paas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/paas.html' target='_blank'/>"


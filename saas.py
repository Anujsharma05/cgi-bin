#!/usr/bin/python
import cgi,os

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
output=data.getvalue('soft')
if output=="firefox":
	print "<META HTTP-EQUIV='refresh' content='0; url=/firefox.sh' target='_blank'/>"

if output=="vlc":
	print "<META HTTP-EQUIV='refresh' content='0; url=/vlc.sh' target='_blank'/>"

if output=="cheese":
	print "<META HTTP-EQUIV='refresh' content='0; url=/cheese.sh' target='_blank'/>"

if output=="office":
	print "<META HTTP-EQUIV='refresh' content='0; url=/office.sh' target='_blank'/>"

if output=="calc":
	print "<META HTTP-EQUIV='refresh' content='0; url=/calc.sh' target='_blank'/>"

if output=="screenshot":
	print "<META HTTP-EQUIV='refresh' content='0; url=/screenshot.sh' target='_blank'/>"

if output=="eog":
	print "<META HTTP-EQUIV='refresh' content='0; url=/eog.sh' target='_blank'/>"
	

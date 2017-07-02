#!/usr/bin/python
import cgi,commands,os

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
name=data.getvalue('d_name')
size=data.getvalue('size')

commands.getstatusoutput('sudo lvcreate -V'+size+'G --name '+name+' --thin blockstorage/blockpool')

commands.getstatusoutput('sudo mkfs.xfs /dev/blockstorage/'+name)

commands.getstatusoutput('sudo mkdir -p /mnt/'+name)

commands.getstatusoutput('sudo mount /dev/blockstorage/'+name+' /mnt/'+name)

entry_check=commands.getstatusoutput('cat /etc/exports | grep ' + name)
if entry_check[0]==0:
	pass
else:
	entry="sudo echo '/mnt/{} *(rw,no_root_squash)' >>/etc/exports".format(name)
	commands.getstatusoutput(entry)


commands.getstatusoutput('sudo systemctl restart nfs-utils')
commands.getstatusoutput('sudo systemctl restart nfs-server')

dir_create="sudo echo 'mkdir -p /media/{}' >/var/www/cgi-bin/object_client.sh".format(name)
commands.getstatusoutput(dir_create)
dir_mount="sudo echo 'mount 192.168.122.163:/mnt/{} /media/{}' >>/var/www/cgi-bin/object_client.sh".format(name,name)
commands.getstatusoutput(dir_mount)

commands.getstatusoutput('sudo tar cvf /var/www/html/object_client.tar object_client.sh') 

print "<META HTTP-EQUIV='refresh' content='0; url=/object_client.tar' target='_blank'/>"

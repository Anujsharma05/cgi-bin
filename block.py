#!/usr/bin/python
import cgi,os,commands

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
name=data.getvalue('drive_name')
size=data.getvalue('drive_size')


commands.getstatusoutput('sudo lvcreate -V'+size+'G --name '+name+' --thin blockstorage/blockpool')
entry_check=commands.getstatusoutput('cat /etc/tgt/targets.conf | grep ' + name)
if entry_check[0]==0:
	pass
else:
	target_entry1="sudo echo '<target {}>' >>/etc/tgt/targets.conf".format(name)
	commands.getstatusoutput(target_entry1)
	target_entry2="sudo echo '	backing-store /dev/blockstorage/{}' >>/etc/tgt/targets.conf".format(name)
	commands.getstatusoutput(target_entry2)
	target_entry3="sudo echo '</target>' >>/etc/tgt/targets.conf"
	commands.getstatusoutput(target_entry3)

commands.getstatusoutput('sudo systemctl restart tgtd')

discover="sudo echo 'iscsiadm --mode discoverydb --type sendtargets --portal 192.168.122.163 --discover' >/var/www/cgi-bin/block_client.sh"
commands.getstatusoutput(discover)
login="sudo echo 'iscsiadm --mode node --targetname {} --portal 192.168.122.163:3260 --login' >>/var/www/cgi-bin/block_client.sh".format(name)
commands.getstatusoutput(login)

commands.getstatusoutput('sudo tar cvf /var/www/html/block_client.tar block_client.sh') 

print "<META HTTP-EQUIV='refresh' content='0; url=/block_client.tar' target='_blank'/>"



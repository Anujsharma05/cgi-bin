#!/usr/bin/python
import cgi,os

print "content-type:text/html\r\n\r\n"
data=cgi.FieldStorage()
name=data.getvalue('os_name')
ram=data.getvalue('os_ram')
core=data.getvalue('os_core')
port=data.getvalue('os_port')
password=data.getvalue('os_password')

if name=="redhat":
	os.system('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.1.qcow2 /var/lib/libvirt/images/'+name+'.qcow2')	
	os.system('sudo virt-install --ram '+ram+' --vcpu '+core+ ' --name ' +name+ ' --disk path=/var/lib/libvirt/images/'+name+'.qcow2 --import --graphics vnc,listen=192.168.122.1,port=6666,password='+password+'&')
	os.system('sudo websockify --web=/usr/share/novnc '+port+' 192.168.122.1:6666')	
else:
	print "wrong os name entered"
	


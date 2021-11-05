import getpass
import telnetlib

#by hicham maaroufi
#iam beginner in network automation..i willl try to share the things i do

host = '192.168.122.22'
user = input('insert username ===> : ')
password = getpass.getpass('insert password => :')

tl = telnetlib.Telnet(host)
tl.write(user.encode('ascii') + b'\n')

if password:
    tl.read_until(b'Password')
    tl.write(password.encode('ascii') + b'\n')

tl.write(b'enable\n')
tl.write(b'cisco\n')
tl.write(b'conf t\n')
#create vlan's
for n in range(2, 6):
    tl.write(b'vlan ' + str(n).encode('ascii') + b'\n')
    tl.write(b'name python_vlan_' + str(n).encode('ascii') + b'\n')

#assign ports to vlans
tl.write(b'int range g0/1 - 3\n')
tl.write(b'switchport mode access\n')
tl.write(b'switchport access vlan 2 \n')

tl.write(b'int range g1/0 - 3\n')
tl.write(b'switchport mode access\n')
tl.write(b'switchport access vlan 3 \n')

tl.write(b'int range g2/0 - 3\n')
tl.write(b'switchport mode access\n')
tl.write(b'switchport access vlan 4 \n')

tl.write(b'end\n')
tl.write(b'exit\n')
print(tl.read_all().decode('ascii'))






#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import getpass
import os, subprocess
import socket
import fcntl
import struct

NEWIPADRESS = ""
SMTPSERVER = ""
SMTPUSER = ""
SMTPPORT = "25"
SMTPPASSWD = ""

def replace_its_bugzilla():
   subprocess.call(['cp','-f','its-bugzilla.jar','/my_services/gerrit/plugins/its-bugzilla.jar'])

def get_ip_address(ifname):
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   return socket.inet_ntoa(fcntl.ioctl(
      s.fileno(),
      0x8915,  # SIOCGIFADDR
      struct.pack('256s', ifname[:15])
   )[20:24])

def fileSetup():
   global NEWIPADRESS
   global SMTPSERVER
   global SMTPUSER
   global SMTPPORT
   global SMTPPASSWD

   SOURCEFILELIST = ['gerrit.config','index.php','params.json','secure.config']
   TARGETFILELIST = ['/my_services/gerrit/etc/gerrit.config','/var/www/html/gerrit/index.php','/my_services/bugzilla/data/params.json','/my_services/gerrit/etc/secure.config']
   CHANGEDFILELIST = []

   # Check if template files are available
   for fileName in SOURCEFILELIST:
      if not os.path.isfile(fileName):
         print fileName + " template file is missing. Aborting..."
         os.exit(99)

   # Check if target files are available
   for fileName in TARGETFILELIST:
      if not os.path.isfile(fileName):
         print fileName + " target file is missing. Aborting..."
         os.exit(99)

   # Read template files and replace info provided by user
   for position in [0,1,2,3]:
      temp = ""
      with open(SOURCEFILELIST[position],'r') as f:
         temp = f.read()
      temp = temp.replace('NEWIPADRESS',NEWIPADRESS)
      temp = temp.replace('SMTPSERVER',SMTPSERVER)
      temp = temp.replace('SMTPUSER',SMTPUSER)
      temp = temp.replace('SMTPPORT',SMTPPORT)
      temp = temp.replace('SMTPPASSWD',SMTPPASSWD)
      CHANGEDFILELIST.append(temp)

   # Replace configuration file content
   for position in [0,1,2,3]:
      temp = ""
      with open(TARGETFILELIST[position],'w') as f:
         f.write(CHANGEDFILELIST[position])


def serviceStop(name):
   pid = ""
   print "Stopping service: " + name
   if name == 'gerrit':
      with open('/my_services/gerrit/logs/gerrit.pid','r') as f:
         pid = f.read()
   elif name == 'apache':
      with open('/var/run/apache2/apache2.pid','r') as f:
         pid = f.read()

   subprocess.call(['service', name, 'stop'])
   if pid != "": subprocess.call(['kill', '-9', pid])

def serviceStart(name):
   print "Starting service: " + name
   subprocess.call(['service', name, 'start'])

def daemonReload():
   print "Reloading daemon configuration..."
   subprocess.call(['systemctl','daemon-reload'])

def main():
   global NEWIPADRESS
   global SMTPSERVER
   global SMTPUSER
   global SMTPPORT
   global SMTPPASSWD

   NEWIPADRESS = get_ip_address('eth0')

   # Request to user Raspberry Pi IP address
   print("\nCurrent Raspberry pi IP address is: " + NEWIPADRESS)
   temp = raw_input('Please enter a different IP address if necessary: ')
   if temp != "": NEWIPADRESS = temp
   print "\nAll services will be available under IP: " + NEWIPADRESS + "\n"

   # Request to user SMTP server data
   temp = raw_input('Please enter your SMTP (e-mail) server address: ')
   if temp != "": SMTPSERVER = temp

   temp = raw_input('Please enter your SMTP (e-mail) server port number (leave blank for default 25): ')
   if temp != "": SMTPPORT = temp

   temp = raw_input('Please enter your SMTP (e-mail) server username: ')
   if temp != "": SMTPUSER = temp

   temp = getpass.getpass('Please enter your SMTP (e-mail) server password: ')
   if temp != "": SMTPPASSWD = temp

   print "\nStopping services..."
   serviceStop('gerrit')
   serviceStop('apache2')
   serviceStop('jobqueue.pl')

   print "\nSetting up configuration files..."
   fileSetup()

   print "\nReplacing its-bugzilla plugin..."
   replace_its_bugzilla()

   daemonReload()

   print "\nStarting services..."
   serviceStart('gerrit')
   serviceStart('apache2')
   serviceStart('jobqueue.pl')

   print "\n"

if __name__ == '__main__':
   main()

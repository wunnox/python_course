##############################################
#
# Name: xml_read.py
#
# Author: Peter Christen
#
# Version: 1.1
# 
# Date: 10.07.2017 V1.0
#       24.06.2026 V1.1 Anpassungen
#
# Purpose: Einlesen eines XML-Files
#
##############################################

import xml.dom.minidom

#### Read the file
doc = xml.dom.minidom.parse("inventory.xml")

#### Analyse the XML data
servers = doc.getElementsByTagName("server")
for server in servers:
        name = server.getAttribute("name")
        nrcpu = server.getElementsByTagName("nrcpu")[0]
        release = server.getElementsByTagName("release")[0]
        system = server.getElementsByTagName("system")[0]
        osfam = server.getElementsByTagName("osfam")[0]
        machine = server.getElementsByTagName("machine")[0]
        timestamp = server.getElementsByTagName("timestamp")[0]
        print (name)
        print (nrcpu.firstChild.data)
        print (release.firstChild.data)
        print (system.firstChild.data)
        print (osfam.firstChild.data)
        print (machine.firstChild.data)
        print (timestamp.firstChild.data)

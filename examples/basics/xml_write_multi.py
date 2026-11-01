#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_xml_write_file_multi.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.07.2017
#
# Purpose: Erstellen eines XML-Files mit mehreren Records
#
##############################################

import xml.dom.minidom

### Creating the first level
doc = xml.dom.minidom.Document()
doc.appendChild(doc.createComment('Inventory data from Server Andromeda'))
first_level = doc.createElement('inventory')
doc.appendChild(first_level)

### Create the second level                                              
second_level = doc.createElement('server')
second_level.setAttribute( 'name', "Andromeda" )
first_level.appendChild(second_level)

### Create data elements
data = {"nrcpu":"10","release":"16.5.0","system":"Darwin","osfam":"posix","machine":"arm64","timestamp":"1782320082"}
for name, value in data.items():
   # Create element
   element_name = doc.createElement(name)
   second_level.appendChild(element_name)

   # Add element value
   element_value = doc.createTextNode(value)
   element_name.appendChild (element_value)

### Create the second level                                              
second_level = doc.createElement('server')
second_level.setAttribute( 'name', "UM00365" )
first_level.appendChild(second_level)

###Datenelemente erstellen
data = {'nrcpu':'4','release':'16.5.0','system':'Darwin','osfam':'posix','machine':'x86_64','timestamp':'1499540600'}
for name,value in data.items():
   # Create element
   element_name = doc.createElement(name)
   second_level.appendChild(element_name)

   # Add element value
   element_value = doc.createTextNode(value)
   element_name.appendChild (element_value)

### Write data to file
doc.writexml( open('inventory.xml', 'w'),
   indent="  ",
   addindent="  ",
   newl='\n')
doc.unlink()

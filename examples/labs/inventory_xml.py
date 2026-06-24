import platform
import multiprocessing
import os
import time
import argparse
import xml.dom.minidom

# Variables
timestamp = time.time()
inventory = {}

# Functions
def getdata():
    ''' Collect data '''

    inventory['name'] = platform.node()
    inventory['nbcpu'] = multiprocessing.cpu_count()
    inventory['system'] = platform.system()
    inventory['release'] = platform.release()
    inventory['osfam'] = os.name
    inventory['machine'] = platform.machine()
    inventory['timestamp'] = int(timestamp)

def showdata():
    ''' Output data '''

    print('#'*15)
    print('Server details')
    print('#'*15)
    print('Name:', inventory['name'])
    print('Nb. of CPUs:', inventory['nbcpu'])
    print('System:', inventory['system'])
    print('Release:', inventory['release'])
    print('Machine:', inventory['machine'])
    print('OS Family:', inventory['osfam'])
    print('Timestamp:', inventory['timestamp'])

def create_xml():
    ''' Create a XML file '''

    print("Create file inventory.xml")

    comment="Server inventory data"

    # Create first level
    doc = xml.dom.minidom.Document()
    doc.appendChild(doc.createComment(comment))
    erste_stuffe = doc.createElement("inventory")
    doc.appendChild(erste_stuffe)

    for data in [inventory]:
        # Create second level
        zweite_stuffe = doc.createElement("server")
        zweite_stuffe.setAttribute( "name", data["name"])
        erste_stuffe.appendChild(zweite_stuffe)

        # Create data elements
        for name,value in data.items():
            # Create elements
            element_name = doc.createElement(name)
            zweite_stuffe.appendChild(element_name)

            # Element Wert hinzufügen
            element_wert = doc.createTextNode(str(value))
            element_name.appendChild(element_wert)

    # Write data to file
    doc.writexml( open('inventory.xml', 'w'),
        indent="  ",
        addindent="  ",
        newl='\n')
    doc.unlink()

if __name__ == "__main__":
    # Evaluate parameters
    parser = argparse.ArgumentParser(description='Reads the inventory data from the current server')
    parser.add_argument('-x', action='store_true', help="Output data in XML file")
    args = parser.parse_args()
    
    # Output data
    getdata()
    if args.x: create_xml()
    else:      showdata()


import platform
import multiprocessing
import os
import time
import argparse
import xml.dom.minidom

# Classes
class Server:
    ''' Server Inventory '''

    # Class variables
    timestamp=time.time()
    inventory={}

    def __init__(self,name):
        self.inventory['name'] = platform.node()
        self.inventory['nbcpu'] = multiprocessing.cpu_count()
        self.inventory['system'] = platform.system()
        self.inventory['release'] = platform.release()
        self.inventory['osfam'] = os.name
        self.inventory['machine'] = platform.machine()
        self.inventory['timestamp'] = int(self.timestamp)

    def showdata(self):
        ''' Output data '''

        print('#'*15)
        print('Server details')
        print('#'*15)
        print('Name:', self.inventory['name'])
        print('Nb. of CPUs:', self.inventory['nbcpu'])
        print('System:', self.inventory['system'])
        print('Release:', self.inventory['release'])
        print('Machine:', self.inventory['machine'])
        print('OS Family:', self.inventory['osfam'])
        print('Timestamp:', self.inventory['timestamp'])

    def create_xml(self):
        ''' Create a XML file '''

        print("Create file inventory.xml")

        comment="Server inventory data"

        # Create first level
        doc = xml.dom.minidom.Document()
        doc.appendChild(doc.createComment(comment))
        erste_stuffe = doc.createElement("inventory")
        doc.appendChild(erste_stuffe)

        for data in [self.inventory]:
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

    # Collect data
    server=Server(platform.node())

    # Output data
    if args.x: server.create_xml()
    else: server.showdata()

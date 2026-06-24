import platform
import multiprocessing
import os
import time
import argparse
import json

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

    def create_json(self):
        ''' Create a JSON file '''

        print("Create file inventory.json")

        with open('inventory.json', 'w') as outfile:
            json.dump(self.inventory, outfile)

if __name__ == "__main__":
    # Evaluate parameters
    parser = argparse.ArgumentParser(description='Reads the inventory data from the current server')
    parser.add_argument('-j', action='store_true', help="Output data in JSON file")
    args = parser.parse_args()

    # Collect data
    server=Server(platform.node())

    # Output data
    if args.j: server.create_json()
    else: server.showdata()

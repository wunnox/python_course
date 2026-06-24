import platform
import multiprocessing
import os
import time
import argparse
import json

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

def create_json():
    ''' Create a JSON file '''

    print("Create file inventory.json")

    with open('inventory.json', 'w') as outfile:
        json.dump(inventory, outfile)

if __name__ == "__main__":
    # Evaluate parameters
    parser = argparse.ArgumentParser(description='Reads the inventory data from the current server')
    parser.add_argument('-j', action='store_true', help="Output data in JSON file")
    args = parser.parse_args()
    
    # Output data
    getdata()
    if args.j: create_json()
    else:      showdata()


import platform
import multiprocessing
import os
import time

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

if __name__ == "__main__":
    # Collect data
    server=Server(platform.node())

    # Output data
    server.showdata()

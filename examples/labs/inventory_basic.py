import platform,multiprocessing,os,time

# Variables
timestamp=time.time()
inventory={}

# Functions
def getdata():
    ''' Collect data '''

    inventory['name']=platform.node()
    inventory['nbcpu']=multiprocessing.cpu_count()
    inventory['system'] = platform.system()
    inventory['release'] = platform.release()
    inventory['osfam'] = os.name
    inventory['machine'] = platform.machine()
    inventory['timestamp'] = int(timestamp)

def showdata():
    ''' Output data '''

    print ('#'*15)
    print ('Server details')
    print ('#'*15)
    print ('Name:',inventory['name'])
    print ('Nb. of CPUs:',inventory['nbcpu'])
    print ('System:',inventory['system'])
    print('Release:', inventory['release'])
    print('Machine:', inventory['machine'])
    print('OS Family:', inventory['osfam'])
    print('Timestamp:', inventory['timestamp'])

if __name__=="__main__":
    # Output data
    getdata()
    showdata()

# Modules 
from time import perf_counter
from multiprocessing import Pool, Pipe

# Variables        
pc = []            # List for prime number counter
pia, pib = Pipe()  # Create a pipe for prime numbers

# Functions
def primecalc(data):
    '''Calculate prime numbers'''
        
    print(f"Searching for prime numbers from {data[0]} to {data[1]}")
    for z in range(data[0], data[1] + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    data[2].send(len(pc))
    data[2].close()

def pool_handler():
    p = Pool(3)
    p.map(primecalc, [(1, 17000, pia), (17001, 24000, pia), (24001, 30000, pia)])
    
if __name__ == "__main__":
    # Start process
    start = perf_counter()
    pool_handler()
    
    # Completion
    numberofprimes = 0 
    
    while pib.poll():
        numberofprimes = numberofprimes + pib.recv()
    
    print(f"{numberofprimes} prime numbers found")
    end = perf_counter()
    print(f"Performance: {round(end - start, 6)} sec")

from concurrent import futures                              
from time import perf_counter
        
max_probe = 30000  # Maximum runs
pc=[]              # List for prime number counters
    
def primrechner(ps,pe):
    '''Calculate prime numbers'''
    
    pc=[]
    print(f"Searching for prime numbers from {ps} to {pe}")
    for z in range(ps,pe+1):
        for z2 in range(2,z):
            if not z%z2: break
        else: pc.append(z)
    return pc

if __name__ == "__main__":
    start = perf_counter()
        
    with futures.ProcessPoolExecutor(max_workers=3) as e:   ### Maximum number of processes
        chunk = 10000                                       ### Chunk size
        fs = {e.submit(primrechner, *(n, n+chunk-1)): n for n in range(1, max_probe, chunk)}
        for f in futures.as_completed(fs):
            pc.extend(f.result())
    
    # Conclusion
    print(f"{len(pc)} prime numbers were found")
    end = perf_counter()
    print(f"Performance: {round(end - start,6)} sec") 

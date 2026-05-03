# Modules
from multiprocessing import Process, Pipe
from time import perf_counter

# Variables
pc = []            # List for prime number counter
pia, pib = Pipe()  # Create pipe for prime numbers

# Functions
def primecalc(ps, pe, pia):
    '''Calculate prime numbers'''

    print(f"Searching for prime numbers from {ps} to {pe}")
    for z in range(ps, pe + 1):
        pc.append(z)
        for z2 in range(2, z):
            if not z % z2:
                pc.remove(z)
                break
    pia.send(len(pc))
    pia.close()

if __name__ == "__main__":
    start = perf_counter()

    # Start processes
    px = Process(target=primecalc, args=(1, 17000, pia))
    px.start()
    px = Process(target=primecalc, args=(17001, 24000, pia))
    px.start()
    px = Process(target=primecalc, args=(24001, 30000, pia))
    px.start()

    # Completion
    numberofprimes = pib.recv()
    numberofprimes = numberofprimes + pib.recv()
    numberofprimes = numberofprimes + pib.recv()

    print(f"{numberofprimes} prime numbers found")
    end = perf_counter()
    print(f"Performance: {round(end - start, 6)} sec")

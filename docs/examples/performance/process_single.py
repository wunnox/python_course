from time import perf_counter

pc=[]  # List for prime number counter

def primrechner(ps,pe):
   '''Calculate prime numbers'''

   print(f"Searching for prime numbers from {ps} to {pe}")
   for z in range(ps, pe+1):
      pc.append(z)
      for z2 in range(2, z):
         if not z % z2: 
            pc.remove(z)
            break

### Start process
start = perf_counter()
primrechner(1, 30000)

### Completion
print(f"{len(pc)} prime numbers were found")
end = perf_counter()
print(f"Performance: {round(end - start, 6)} sec")

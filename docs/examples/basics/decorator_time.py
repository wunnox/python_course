import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__}: {end_time - start_time} Seconds")
        return result
    return wrapper
    
@timer_decorator
def quadrat(n):
   for i in n:
      yield (i*i)
      
res=quadrat([10,20,30,40])
for num in res:
   print(num)

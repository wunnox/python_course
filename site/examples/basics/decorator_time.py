import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Runtime of {func.__name__}: {round(end_time - start_time,6)} Seconds")
        return result
    return wrapper
    
@timer_decorator
def square(n):
   for i in n:
      yield (i*i)
      
res=square([10,20,30,40])
for number in res:
   print(number)

def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in der Function {func.__name__}: {str(e)}, return 1")
            return 1
    return wrapper

@handle_exceptions
def divide(a, b):
    return a / b

for i in (3,0,7):
    print(divide(10, i))

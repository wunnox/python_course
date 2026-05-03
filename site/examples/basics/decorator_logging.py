import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='decorator_test.log'
    )
logger = logging.getLogger('test_logger')

def log_function_call(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_message=f"Function {func.__name__} called Argument {args}. Result: {result}"
        logger.info(log_message)
        return result
    return wrapper

@log_function_call
def message(name):
    return f"Hello, {name}!"

print(message("Max"))

import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='Example.log'
    )
logger = logging.getLogger('my_logger')

name='Peter'
print(f"Hello {name}")
logger.info(f'Hello {name}')

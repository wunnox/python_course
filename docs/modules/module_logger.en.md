# Module Logger

This module can be used to generate log messages

```python
import logging

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='Example.log'
    )
logger = logging.getLogger('my_logger')

name='Max'
print(f"Hello {name}")
logger.info(f'Hello {name}')
```

Download: [logger.py](../examples/modules/module_logger.py)

## Explanation:

These lines in the function configure the basic logging system:

 - level=logging.INFO: Sets the logging level to INFO. This means that messages with the levels INFO, WARNING, ERROR and CRITICAL are logged.
 - format=...: Defines the format of the log entries. This includes the timestamp, logger name, log level and the actual message.
 - datefmt=“%Y-%m-%d %H:%M:%S”: Specifies the format for the timestamp.
 - filename=“apply.log”: Specifies that the log entries should be written to a file named “apply.log”.

A log message is then created:

 - name=“Peter”: Assigns the value “Peter” to the variable name.
 - print(f‘Hello {name}’): Outputs ‘Hello Peter’ to the console.
 
- logger.info(f'Hello {name}“): Writes a log entry with the INFO level and the text ‘Hello Peter’ to the log file.

```text
2024-11-01 12:34:56 - my_logger - INFO - Hello Peter
```

## Available logging levels

The Python logging module offers five main logging levels, arranged in ascending order of severity. These levels are:

1. DEBUG (10)
2. INFO (20)
3. WARNING (30)
4. ERROR (40)
5. CRITICAL (50)

Here are the details for each level:

DEBUG (10)
This is the lowest logging level. It is used to provide detailed information for diagnosing problems. Typically, it is used during development and debugging.

INFO (20)
This level is used for general information confirming that the programme is functioning as expected.

WARNING (30)
WARNING is the standard logging level. It is used to indicate that something unexpected has occurred or that a problem may arise in the near future (e.g. ‘Disk space low’).

ERROR (40)
This level is used when a serious problem has occurred that has prevented a specific function from executing.

CRITICAL (50)
This is the highest logging level. It is used to log very serious errors that may result in the programme no longer being able to run

It is important to note that each level has numerical values (shown in brackets) representing its severity. A logger or handler with a specific level will log all messages of that level and higher. Additionally, there is a special level:

NOTSET (0)
This level is used when no specific level has been set for a logger. In this case, the logger uses the level of its parent logger

When configuring logging, you can specify the desired level to control which types of messages should be logged. For example, if you set the level to WARNING, only messages of the levels WARNING, ERROR and CRITICAL will be logged, whilst DEBUG and INFO are ignored.

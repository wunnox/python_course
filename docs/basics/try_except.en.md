# try - except

The `try/except` statement is used in Python for error handling.
 - The `try` block contains code that could raise an exception.
 - If an error occurs, the `try` block is terminated and the corresponding `except` block is executed, rather than the programme crashing.
 - If no error occurs, the `except` block is skipped and the programme continues as normal.

## Example script

- [try_except.py](../examples/basics/try_except.py) 

### Explanation

- In the `try` block, the file is opened, its contents are read, and converted to an integer using `int(...)`. Both file and conversion errors may occur here.
- The first except FileNotFoundError handles the case where the file does not exist, raises an exception and returns None. (Optional)
- The second except ValueError handles the case where the read content is not a valid integer, raises an exception and returns None. (Optional)
- The else block is only executed if no error occurs in the try block: the number has been successfully read and is printed and returned. (Optional)
- The finally block always runs, regardless of whether an error has occurred or not, and attempts to close the file again; if f does not exist at all due to an earlier error, the UnboundLocalError is silently ignored. This ensures that resources (in this case, the file) are reliably cleaned up. (Optional)
- The except Exception as e block is required at the very least if no other except block exists; it is also possible to use just except. The other blocks are optional and can be omitted if necessary.

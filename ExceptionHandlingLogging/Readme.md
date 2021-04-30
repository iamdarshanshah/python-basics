## Exceptions (Runtime Error)

- A class in python
    - user defined
    - predefined
- use `try` and `except` block to handle exceptions
- optinally `else` block is used for executing statements when exception is not raised
- `finally` block will be used for all the mandatory executions to  be performed
- Syntax :-
```buildoutcfg
try:
    code that will raise an exception
except <Exception>:
    handler statements
else:
    Statements when exception doesn't occur
finally:
    mandatory executions

```

## Exception Hierarchy

- BaseException
    - Exception
        - StandardError
            - EOFError
            - ZeroDivisionError
            - IndentationError
        - Warning
            - DeprecatedWarning
            - ImportWarning
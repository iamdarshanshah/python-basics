## Command Line arguments
- Arguments which are passed when running a python program using python cli.
```buildoutcfg
> python myProgram.py 123 xyz ab [1,2,3]
```
- arguments are passed through a list `argv`
- `argv` is present in `sys` module.
```buildoutcfg
import sys
cmdArgList = sys.argv
1stArg = sys.argv[0]
```
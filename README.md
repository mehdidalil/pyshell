# pyshell
a minimal implementation of csh in python
```
python3 pyshell.py
```
## builtins
#### cd [directory]
no options implemented now
#### env [-i] [name=value]... [executable [argument...]]
the env builtin shall obtain the current environment, modify it according to its arguments, then invoke the utility named by the utility operand with the modified environment.

If the [-i] option is specified, env invoke executable with exactly the environment specified by the [name=value] arguments
#### setenv [name] [value]
#### unsetenv [name]
#### echo [-n] [string...]
if the [-n] option is specified, no newline at the end will be printed
#### exit [status]
exit the shell with the latest return value known

if status is specified, will exit the process with status value
#### tictactoe
a little tictactoe game for 2 players

## operators
#### semicolon [;]
separates commands execution


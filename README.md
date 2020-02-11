# pyshell
a minimal implementation of csh in python

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

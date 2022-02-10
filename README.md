# PIG
dont use this

```
test.pigg
- VARSTORSTRING.Vpigg
- VARSTORINT.Vpigg
- VARSTORINP.Vpigg
- RUNIF.Vpigg
______________________

new string test = Hello 
call string test

# output

Hello
```

# TODO 

- Var management system
- Assign strings
- Assign Integers
- User Input

Currently working on:
> Var management system

# var mangangment system

We have two types of variables, strings and integers.

## Integers
Can have two states

- public, prints to the terminal autmaticaly
- private, stores a variable in the memory

### Private Integer (extra)

- be able to add on a value
- be able to erase it from the memory

# What is it for?
I am making pig as experience for programming as the only other "big" project that I made
was a password maker / manager that I made over a year ago. Since then I have expanded my
reach and I want to test that.

# Files how to?
To create a pig file do the following:

- Make a new folder (the name doesn't matter)
- And in the folder make a file with the file extension .pigg
- In the following file, I will show you some basic syntax to put in
```
add 5, 5
subtract 15, 5
divide 20, 2
multi 5, 2

println('Hello world')

new string Hello = Hello world
call string Hello

new integer public age = 99999999
call integer age

new integer private Youcantseeme = 0
call integer private Youcantseeme
```
- Then copy pig.py from src in pig
- paste it into your folder with the .pigg file in it
- run the pig.py file
- it will open a window and close it
- but it will also create a new .bat file called build
- this is what you open now to compile your file

# Things that need to be implemented:
- build.bat file
- if statements
- other things
- comments
- while loops
- (maybe) for loops
- github

# What Is Bash script
---
- Bash = bourne again shell
- shell:-is used to command and talk  or monitore with the kernel.
- Script:- is a file that contains shell commands in a simple and clear algorithm.
- derived from "sh":-bourne shell.
-  `.sh`:file extension for bash.
- executable permissions is a must 'x'.
- we can use any text editors.
# Use Of Bash For Hackers
--- 
- to develop script.
- automating tasks.
- simplify your linux ability.
- dev hacking scripts.

# Output
--- 
- shebang : `#! /bin/bash`:- to start the bash script & it uses to tell the shell which interpreter we are using is sh / zsh/ fish... 
- `echo " add text " `:to display any text on bash.
- `echo` to start with new line.
- 1. `/bin/bash file name`:to run file
- 2. `./ file name`:denied must get execute permission
- 3. `bash file name`:denied must get execute permission
# Variables & Datatype
--- 
### Variables
`Variables`: are computer memory location.
         : bash variables are string by default.
         : Variables_name=value; must be without space.
         :and only double quote.
         :never start with numbers.
         : to call them we use a dollar sign($) in front of the var_name and to stick it with other text use $[var_name]
`Set`: can be used to assign values to positional parameters.
![[Pasted image 20240813211843.png]]
`System Variables`: are variables those are declared by the system.
![[Pasted image 20240813213921.png]]

![[Pasted image 20240813214101.png]]
- USER: displays computer owner(host).
### DataTypes
- they create strings only.
- `Arrays`: are lists or tuples on python.
        ![[Pasted image 20240813214940.png]]
        ![[Pasted image 20240813215251.png]]
# Input
---
- Two Types of input handling.
     1. `Read function`
         - is same as input in python.
         - accept values while the script is running.
         - ![[Pasted image 20240813220834.png]]
	 2. `Argument`
	     - is same as argu in python.
	     - helps to get input before the script starts.
	     - use $0 - $9 while u want to work with the input.
	     - ![[Pasted image 20240814102336.png]]

# Comment And Indentations
---
### Comment
   - "#": for one line.
   - "<<COMMENTS ...... COMMENTS": for many lines.
   `sleep`: make a good waiting on our script.
         ![[Pasted image 20240813224644.png]]
### Indentation


# Arithmetic Operation
--- 
#### Operation
- Syntax: `$((expression))`
- `let`: to assigning variables.

### A. Arithmetic operations 

- ![[Pasted image 20240814103548.png]]

### B. Assignment operations
- ![[Pasted image 20240814103652.png]]
### C. Comparison Operation
1. `ALPHABETIC COMPARISION`
     ![[Pasted image 20240814104051.png]]
2. `SIGN COMPARISON`
     ![[Pasted image 20240814104128.png]]

# If-else
---
- syntax:
![[Pasted image 20240814105259.png]]
- if we use `[condition]`for the conditions we will use alphabetic comparison.
- if we use `(())` to compare for the conditions we must use symbols to compare. 
- Nested if : use of if adding other if with out closing the open one then when we close the first one we must also close the next one. 























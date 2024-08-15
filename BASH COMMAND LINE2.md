# FURTHER ON BASH
2.1.Regular Expressions
2.2.Else if
2.3.Loops
2.4.Functions
2.5.Bash and Linux Shell

# Regular Expressions
---
-`regex`: to filter validation on any platform.
-are patterns that helps to filter texts, newlines, tabs(space between words)& symbols.
-also used in Linux tools called ==(grep, awk & sed)==. 
-`Metacharacters`: are the regex pattern symbols for filter.
     - example: \n,\t .... they are the pattern.
- ![[Pasted image 20240814202752.png]]
-regex on python programming language>>>
   ![[Pasted image 20240815112606.png]]

`The Metacharacters`
---
1. ( . ) : give me ==all lines== except the new lines without with text. 
      -syntax: (.)
2. ( ^ )`assertion`: to ==get lines== but only shaded or highlight with the given word ==that start with== not the word we give that found in between pattern we give on the space.
     -syntax: (^###)
3. ( $ )`assertion`: to ==get line that only ends== with some pattern.
     -syntax: (" ###$")
4. (  *  )`quantity`:  to get line that have pattern that ==occurs 0 and more times==.
     -syntax: (### * )
5. ( + )`quantity`:get lines that have pattern that ==occurs 1 and more times==.
     -syntax: (^###+) -start with it
            : (### +) -also in between  
6. ( ? )`quantity`: the last pattern ==occurs 0 and 1 times==. 
     -syntax: (### ?)
7. ( .* & .+): which starts with the pattern and all next to it. 
     -syntax: (^###.* )
     -![[Pasted image 20240814205606.png]]
![[Pasted image 20240814205918.png]] 
     
8. curly bracket{min, max} `quantity`: to customize by our self
      -syntax: (###{min, max})    
      - {0,1}=?
      - {1,}=+ (empty space is as infinity)
    -![[Pasted image 20240815122211.png]]

9. ( `\w`): used to get alphanumeric without newlines and symbols and also tabs.
     -syntax:  (`\w`)
10. (`\W`): used to get ALL(tabs , symbols, newline) without the alphanumeric.
     -syntax:  (`\W`)
11. (`\s`): only whitespaces.
     -syntax:  (`\s`)
12. (`\S`): all without the whitespaces.
      -syntax:  (`\S`)
13. (`\d`): used to get only digits.
     -syntax:  (`\d`)
14. (`\D`): used to get without numbers.
15. pipe( | )`or`: used to search to different things.
     -syntax:  (A | B)
16. Escape( `\` ): to search symbols that are metacharacters.
     -syntax:  (`\sign`) 
17. square brackets( [] )`custom pattern`:create your own patterns.
      -syntax: [pattern]
  
      Exerscise one
    A.
     ![[Pasted image 20240815132510.png]]
    B.
     ![[Pasted image 20240815133007.png]]
    C.
     ![[Pasted image 20240815133052.png]]
#### Bash regex
---
-we must use `escape '\'` infront of the metacharacters that have other work in Lunix.
   - `BASH FOR REGEX`: we use =="=~"== for regex check for with if condition statements.
                 : we use double brackets for conditional statements.
                syntax:
                     ![[Pasted image 20240815135204.png]]

# Bash Else if
---
- `elif`: to use more than one comparing.
- Syntax:
- ![[Pasted image 20240814221320.png]]

# Loops
---
1. `FOR LOOP`
    - for num in {1..10}
      do
      echo $num
      done
	![[Pasted image 20240814221430.png]]
    ![[Pasted image 20240814221728.png]]
- for loop without sequence data
   -`for((i = 1`start`; i<=10 `end`; i++ `increm...`))`
   -index slicing({start..stop..step})


2. `WHILE LOOP`
- Syntax: 
![[Pasted image 20240814222921.png]]
- Break Statement:
   -![[Pasted image 20240814223408.png]]

- continue statement == pass
3. `UNTIL LOOP`
     - ![[Pasted image 20240815151924.png]]
     - when the expression is true the loop exits.
# Functions
---
- Syntax:
  ![[Pasted image 20240815152142.png]]
- if we use `$?` : it will display the return value that is in the funtion. 

# Bash and Linux 
---
- We can run linux commands inside our bash.
   -"apt update"
- As lambda we can run the for loop on bash code in one line.
- `echo *`: we can access files in current directory .
- we can interact with linux terminal using bash, but our terminal must be on bash.
   -"/bin/bash"
- we can also run for loop on linux terminal.
   -syntax:![[Pasted image 20240815172601.png]]
- `echo $PWD` tell us current directory.









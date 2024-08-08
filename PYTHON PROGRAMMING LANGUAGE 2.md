### CORE PYTHON PROGRAMMING LANGUAGE
2.1. INDEXING AND SLLICING {STARTING, STOP,STEP}
2.2. INPUT HANDLING {2 METHODS}
2.3. OPERATIONS
2.4. INDENTATION
2.5. IF ELSE
2.6. ERRORS (EXCEPTIONS)
2.7. ERROR HANDLING
2.8. LOOPS
# 2.1. INDEXING AND SLLICING {STARTING, STOP,STEP}
---
-`Indexing`:
![[Pasted image 20240807200955.png]]
- the negative and positive indexing is reverse counting to display it on terminal 
     -for negative index started from the last{right}
     -for positive index starts from {left}
- we can use index concept in strings and tuples.
-`Slicing`:
![[Pasted image 20240807202204.png]]
-print(variable name[start : stop : step])
-VN[start : stop ]

![[Pasted image 20240807204745.png]]

![[Pasted image 20240807210319.png]]
# 2.2. INPUT HANDLING {2 METHODS}
---
![[Pasted image 20240807210350.png]]

![[Pasted image 20240807210842.png]]
- The `eval()` input type:- is same as changing the data type to `int()`.
![[Pasted image 20240807211617.png]]
![[Pasted image 20240807212314.png]]
![[Pasted image 20240807212505.png]]

![[Pasted image 20240807212835.png]]


# 2.3. OPERATIONS
---
- A. Aritimatic Operators
- B. Assignment Operators
- C. Comparison Operators
  ![[Pasted image 20240807215442.png]]
- D. Logical Operators
  ![[Pasted image 20240807220003.png]]

![[Pasted image 20240807220309.png]]
E. Bitwise Operators
 ![[Pasted image 20240807220640.png]]
0b:-is to tell us that it is a binary number
bitwise- it used to do maths(logical operation) on binary expresstions.

`Complement(Not)(~)`: it will add the number we give it then makes it negative.
                  -convert the first value to binary and it will reverse each bit then converts to decimal.
`And(&)`: we can fill the gap if the binary number is not up to 4 digits.
`Or(|)`: same as and but the logical operator will change.
`^`: if it is same=0 but different is=1
`<<`: it round the after point zeros to the left
`>>`: it is opposite of the << so it rounds to the right

# 2.4. INDENTATION
---
- are just whitespace which python uses for some of its functions

# 2.5. IF ELSE
--- 
-if statement
-if else statement
-if elif statement
# 2.6. ERRORS (EXCEPTIONS)
---
`Logical errors`: is errors when we try to do mathematical works or are like runtime errors.
`The basic errors are`:
->index error
->zero division error
->name error
# 2.7. ERROR HANDLING
---
   ->try & except: `to give our own way of terminal error telling.
# 2.8. LOOPS
---
Types of loops:
  1. `For Loop`
- range keyword: is a series of values between two numeric intervals.
- len(list) keyword: to show the length of a sequence  
  2. `While Loop`
Difference between the for loop and while loops:
 `While loop`                                                        `For loop`                    
1. We can do Infinite loops                              `A.`  Used when only the number of                                                                                 iterations is known.
2. Can be used when the number of                `B.`  Unconditional  
   iteration are unknown.(conditional)              `C.` Ends when the iterable is                                                                                         finished
3. Ends when the conditions false

-Break keyword


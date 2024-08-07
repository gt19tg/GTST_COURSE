5.1. FURTHER ON USER MANAGEMENT 
5.2.  LINUX FILE OWNERSHIP + PERMISSIONS
5.3. SOFTWARE INSTALLATION
# A. Further on user management 
---
- sudo useradd:- in spirit mood which means their will not be any detail things in it  doesn't appear on"/home directory ".
- sudo adduser:- it a can be created in more detailed manner and it can also appear on "/home directory ".
![[Pasted image 20240731202254.png]]
- id kana:- to see the id number
- cat /etc/passwd:-to know the created users with useradd
- /etc/shadow:- passwords encrypted
- sudo mkdir /home/baba:- to create home directory// ERROR
- sudo mkhomedir_helper username
- su - username: to login with other account
- exit command to get back to first username
- sudo usermod caleb -s /bin/bash:- to change shell type
- cd .. home directory
- echo $SHELL:- to know shell type
- sudors file:-it's other name linux addmensterater file user for giving sudo permission to other users.
![[Pasted image 20240731204341.png]]

![[Pasted image 20240731205205.png]]


# B. Linux File Ownership + Permissions
---

![[Pasted image 20240731210527.png]]

1. ![[Pasted image 20240731210617.png]]
- sudo chown username:-lemaweres - for the user
- sudo chown caleb:caleb abdisa.txt- both

2. ![[Pasted image 20240731211533.png]]

 - (-) file
 - (d) directery/folder
 -parts of![[Pasted image 20240731211829.png]]
-![[Pasted image 20240731212241.png]]

- sudo chmod +x{(excute permission)(-x:xpermistion deleted)} file name

![[Pasted image 20240731213026.png]]


**Numeric permission**![[ Pasted image 20240731212845.png]]
![[Pasted image 20240731213257.png]]

**Symbolic Permission**
![[Pasted image 20240731213421.png]]
[rwx]- read write execute


**Special File Permissions**
![[Pasted image 20240731215425.png]]
-the execution 

# C. Software Installation
---
![[Pasted image 20240731220904.png]]

![[Pasted image 20240731221456.png]]
- Repository:- sites applications are downloaded

![[Pasted image 20240731221640.png]]

![[Pasted image 20240731222257.png]]

![[Pasted image 20240731222629.png]]









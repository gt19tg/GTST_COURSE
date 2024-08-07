#### OVERVIEW OF KALILINUX
_ _ _
5 Phases of ethical hacking:
1. info gathering
2. scanning
3. gaining access
4. Maintaning access
5. cleaning track

1)Information Gathering(reconisence)
  -The first Hacking Phases:
  -in sys, network & host
  ex_tools:-dmitry, ike-scan, legion, maltego, netdiscover, nmap, p0f, recon-ng, spiderfoot
2)Vulnerability Analysis
  ex_tools:-legion, lynis, nikto, nmap, unix-prives....
3)Web Application Analysis
 -finding vulnerabilities and exploits on websites.
 
 ex:-burpsuite, commix, httrack, paros, skipfish, sqlmap, webscarab, wpscan, Zap Database Assessment
4)Database Assessmnet
   -vulnerability and exploits on databases
    ex:-jsql injection, mdb-sql, Oscanner, sidguesser, sqlmap....
5)Password attacks
    -tools for exploiting passwords for login, websites, application, windows
    ex:-john the reeper, johnny, hashcat
6)Wirless Attacks
    -wifi, bluetooth
    ex:-aircrack-ng, wifite, reaver
7)Reverse eng
    -exploiting softwares, mobil applications
    ex:-apktool, NASM Shell
8)Exploitation(attack)
    -exploiting softwaews, mobiles, computers, websites ...
    ex:-sqlmap, searchsploit,metasploit
9)sniffing and spoofing
    -listening orhijacking network
    ex:-wireshark
10)POST exploitation(maintaning access)
    -Tools for listening or hijacking networks
    ex:-backdoor, powersploit
11)Forensics
    -doing researches and investigate a cyber attacks.
    -ex:-autopsy, binwalk, bulk_extrac, chkrootkit, foremost, galleta, hashdeep
12)Reporting tools
     -reort preparation.
     -ex:-recordmydesktop, maltego, faraday IDE, dradis fram , cutycacpt, pipal
13)Social enginn... tools
     -backdoor, maltego
14)System services
    -buttons used to start some sesrvices.
     -ex:-beef start/stop, dradis start/stop
15)Usually used applications
     -softwares for some basic purposes

FOLDER MANAGERS
-dolphen
-thunar
-nautilus

### LINUX COMMAND BASICS
- - - -
A. Parts of terminal 
1) Username
2) hostname
3) current Directory
4) Priviledge
    "$" : local user
    "#" : being root
    "[~]" : tilda, on home directory /home/someuser
    "." : local directory with
    "*" : all directory
5) command place " _ "

B. Linux command basics 
-- every command has option and argument.
COMMAND: small programs that do one task well.
### Command List
1) ls/list directory(folder)
    -ls[OPTION]... [File]...
    -ls -l //
    -ls -a(.nsdnknvk) hidden files
    -ls -filename
    -ls -R: all file in side the files/recursive/
    -ls - Rla
2) cd/ change directory
     cd / :root
     cd : home
     cd .. : 1x back
     cd ../.. : 2x back
     cd "foldername"
3) Pwd / print working directory
  - current directory
4) echo[option][string]
     - used to display line of text / string that are passed as an argument.
     -   create file and add text.
     -echo text >file.txt
     > save 
     - add text >> file.txt  
5) cat/head/tail/less
    -cat : content 
    -head : only the first line text it showes me 
    -wc tail : the last one
    -less = cat
6) touch 
      -to create a file.
      -with out and added file
7) Mkdir / make directory
      - mkdir[folder-name1]...
      - ""a
8) clear
9) rm/remove
    -to remove or delet file
    rm -r =in folders
    rm -i =by permition
    rm -f =force delete
    rm -rf filename
10) cp(copy) | mv(move)
     -(~/)
11) grep (global search for regular expresstion)
     - to search and filter
     - grep-:case insensitive
     - grep-c: count numbers
     - grep-l: displays filename
     - grep-R: search text in folder
     - grep-v: to display without this term
     - grep-n: to display the term find number
12) Wc-word count
     -"no of lines , word count,  byte(storage)  and characters count"
     -line(-l), word(-w), byte(-c)
     -wc -l,w,c

13) sed(stream editor)
    -to filter and modify text
    -Syntax: sed [options] 'command' file(s)
    -sed 's/old/new/g' file.txt (replaces all occurrences of "old" with "new" in file.txt)
14) awk=cat
    -to create filters to write scripts
    -Syntax: awk [options] 'program' file(s)
    -Example: awk '{print $1, $3}' file.txt (prints the first and third fields of each line in file.txt)
    -to print a specific feild
15) tee
    -used to split the output of a command and send it to both the terminal and a file.
    -Syntax: command | tee file(s)
    -Example: ls -l | tee output.txt (displays the long listing of files and also saves it to output.txt)

#### MULTIPLE COMMAND EXECUTIONS
- - - 
MCE(multiple command executions)
     - run multiple commands in 1 line.
     - AND( && ), OR( || ) & PIPEING( | )
         1) AND
         2) OR
         3) PIPEING

















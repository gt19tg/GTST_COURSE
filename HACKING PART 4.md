 s2Day3Malware.md
# MALWARE THREATS
4.1. WHAT IS MALWARE
4.2. KINDS OF MALWARES
4.3. HOW DO THEY INFECT HOSTS / INFECTION TECHNIQUES
4.4. HOW DO THEY HIDE
4.5.ANTI-VIRUS(AV) SOFTWARES
4.6. DETECTION AND PREVENTION
4.7. MALWARES IN HISTORY
4.8. PYTHON FOR MALWARE DEVELOPMENT
4.9. MALWARE ANALYSIS
4.10. MALWARE ANALYSIS TECHNIQUES


## 4.1. WHAT IS MALWARE
---
-`MALWARE`:comes from 'malicious= bad thing ', 'software=set of instruction'
-'mal -ware'
-They can do:
-![[Pasted image 20240901185057.png]]

## 4.2. KINDS OF MALWARES
---
-Based on their propagation/infection and attack:
![[Pasted image 20240901185151.png]]
- A) Trojan: malicious code seems good in the front of the interface.
    1. Backdoor:
    2. Mailfinder: they still emails
    3. Remote Access: C2 servers(Command and Control)
    4. Trojan Banker: takes finandial account
- B) Worm: it jumps in LAN networks
- C) Virus: ![[Pasted image 20240901220852.png]]
        -Common types of virus:
          1. Resident virus and nonresident virus
          2. Multipartite virus
          3. Browser hijacker
- D) Ransomware
- E) Rootkit: malicious software
- F) Adware: 
- G) Botnet
## 4.3. HOW DO THEY INFECT HOSTS /INFECTION TECHNIQUES
---
- the techniques:
   -USB drop attack
   -Spam emails
   -Malicious office macros
   -Software/application from unsafe websites
      ->torrent sites
   -Using cracked software   
   -Malicious browser extension




## 4.4. HOW DO THEY HIDE
---
## 4.5. ANTI-VIRUS(AV) SOFTWEARS
---
-![[Pasted image 20240901225046.png]]
-the second one is behavior based detection.
-Anti-virus evasion techniques:
1. packers: compresses an excutable.
     -behaviourly detected
     -it changes it's signitures/hash/
2. Crypters/encoders: XOR cipher its goal is to change the binary fingerprint of a file to avoid detection.
3. Polymorphic malware: when their is no consistent pattern for the antivirus to recognize.
4. Downloaders and droppers
5. Fileless Malware: straight in the memory




## 4.6. DETECTION AND PREVENTION
---
PREVENTION:
![[Pasted image 20240902090153.png]]
## 4.7. MALWARES IN HISTORY
---
1. Morris Worm: internet worm.
2. ILOVEYOU: virus by email, file cooraption.
3. Stuxnet: is worm. 
4. WannaCry: ransomware.
## 4.8. PYTHON FOR MALWARE DEVELOPMENT
---
->1st understand what the malware have to do.
->2nd choose the malware purposes
     a)`delete files`
     b)`encrypt files`
     c)`corrupt files`
->3rd change the python file to executable(exe) by py2exe technics.
`#1..A) DELETE FILES`        
`#2..B) ENCRYPT FILES`
`#3..C) CORRUPT FILES1`

![[Pasted image 20240902104707.png]]        
->==File Handling in python==
     -Syntax: with open("fileName or filePath", 'x')
     -![[Pasted image 20240902103139.png]]
->Write on files
      ![[Pasted image 20240902103459.png]]
      ![[Pasted image 20240902103528.png]]
->READING FILES
![[Pasted image 20240902103709.png]]
->CREATING FILE
![[Pasted image 20240902104103.png]]
->CHECKING EXISTENCE
![[Pasted image 20240902104221.png]]
![[Pasted image 20240902104751.png]]
-![[Pasted image 20240902105419.png]]
## 4.9. MALWARE ANALYSIS
---
-Malware analyst

## 4.10. MALWARE ANALYSIS TECHNIQUES
---
1. Static MA
A)Basic static analysis:
      ![[Pasted image 20240902105906.png]]
B)Advanced static analysis:
    ![[Pasted image 20240902110021.png]]
2. Dynamic MA
-Basic dynamic analysis:
-Advanced dynamic analysis:













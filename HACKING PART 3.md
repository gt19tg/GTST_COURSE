 s2Day2_Scan.md
# SCANNING AND ENUMERATION 
3.1. WHAT IS SCANNING?
3.2. WHY DO WE SCAN?
3.3. NETWORK SCANNING
3.4. NMAP
3.5. HOST DETECTION
3.6. PORT DETECTION
3.7.OS DETECTION
3.8. BANNER GRABBING
3.9. NSE
3.10. FIREWALL EVASION TECHNIQUES

## 3.1. WHAT IS SCANNING?
---
- `Scanning`: 2nd phase of hacking.
- tests a system based on the info we gathered, helps also to gather more infos.
- is also package of techniques(procedures) to identify hosts, ports and various services within a system.
- ![[Pasted image 20240901073326.png]]

## 3.2. WHY DO WE SCAN?
---
 - ![[Pasted image 20240901073418.png]]
## 3.3. NETWORK SCANNING
---
  -false positive: it help us to scan their is a vulnerability but their is not.
  -scanning methods and tools for different purpose:![[Pasted image 20240901073804.png]]
## 3.4. NMAP
---
![[Pasted image 20240901074041.png]]

- ![[Pasted image 20240901074109.png]]
- ![[Pasted image 20240901074239.png]]
1. LIVE SYSTEM DISCOVERY (host discovery):
     -PING SWEEP:![[Pasted image 20240901074857.png]]
     -![[Pasted image 20240901075005.png]]
     - icmp: is when it sends echo request.
-SYNTAX for NMAP PING SWEEP:
- nmap -sn IP 
- -sn = no port 
- nmap scanme.nmap.org  ===> scanme.nmap.org:is the domain name.
                    ===> and its IP address      


## 3.5. HOST DETECTION
---
- used basicaly for class C.         ![[Pasted image 20240901090621.png]]
- ![[Pasted image 20240901090729.png]]
- network bits depends on IP class.
- live discovery
A. warrning +=1
![[Pasted image 20240901101035.png]]
B. warrning ++
![[Pasted image 20240901100915.png]]

## 3.6. PORT DETECTION
---
- PORT:- process-specific or an application-specific. 
      -uses transport layer
      -udp/tcp
      -65,536 ports
      -1-1024= are reserved ports
    ![[Pasted image 20240901101719.png]]
![[Pasted image 20240901101741.png]]
PORT STATUS(NMAP) when nmap sees:
1. `open port`
-open port discovery: ![[Pasted image 20240901102616.png]]
-to connect to that port.
![[Pasted image 20240901103225.png]]
2. `closed port`
3. `filtered port`: not open or cloesed
---
  SCANNING METHODS
  ---
A. TCP CONNECT(TCP SCAN)
* Relilable because it have ==3way handshake==.
* syntax:
    * nmap -sT IP
B. TCPSYN(STEALTH SCAN)
 - syntax:
    - sudo nmap -sS IP
- we send the RESET flag than the ACK flag.
C. UDP SCAN
- ![[Pasted image 20240901113920.png]]
 - syntax: sudo nmap -sU IP
 - syntax to do udp and tcp sacn to gather are
D. XMAS SCAN
 -  first thing to send is FIN/PSH/URG instead of SYN.
 - RST response shows the system is closed 
 - No response showes is open
 - syntax: sudo nmap -sX IP


## 3.7.OS DETECTION
---
-Syntax:
  * sudo nmap -O IP: os detection
  * sudo nmap -A IP: os detection including version
      
## 3.8. BANNER GRABBING
---
* On the version detaction `BANNER GRABBING`
    Scan Speeds:
    -After sending 1 packets to a host it have a time waiting.
![[Pasted image 20240901124436.png]]
A. Nmap Insane
- nmap -T5 IP
- waits only 0.3sec for the response.
- scannes in 15 min.
B. Nmap Aggressive
- nmap -T4 IP
- waites only 1.25 sec for response.
C. Nmap Normal 
- nmap -T3 IP
- defult speed
D. Nmap Polite and Sneaky
- the slowest timing
- nmap -T2 IP
- nmap -T1 IP
- uses for risky projectes
## 3.9. NSE(Nmap Script Engine)
---
- written with lua-programming language.
- Syntax:
     - nmap -sC IP
     - namp --scriptname.nse IP
     - Nmap -p 22 --script ssh* IP
- usr/share/nmap/scripts
- ![[Pasted image 20240901130844.png]]
- ![[Pasted image 20240901130931.png]]
- Nmap Outputs:
     - ![[Pasted image 20240901131310.png]]

- Nmap Verbose:
    - to display more infos
      - Syntax:![[Pasted image 20240901131533.png]]
   
## 3.10. FIREWALL EVASION TECHNIQUES
---
- Advanced Nmap.
- ![[Pasted image 20240901134416.png]]
- ![[Pasted image 20240901134947.png]]
1. Decoy Scan:
     - Syntax:![[Pasted image 20240901135104.png]]

     - To Use random IP's:
       ![[Pasted image 20240901135155.png]]

2. Fragment packets:
      -IPS: sends the info to level 2 soc analiysts.
      -![[Pasted image 20240901135632.png]]
3. .MAC address Spoofing:
     -using false mac address
     -![[Pasted image 20240901135856.png]]


4. Source Port Manipulation: 
     -![[Pasted image 20240901154505.png]]












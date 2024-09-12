7.1. WHAT IS NETWORK HACKING?
7.2. NETWORK FOOTPRINTING
7.3. NETWORK SNIFFIING
7.4. NETWORK CAPTURES
7.5. MAC ATTACK
7.6. ARP POISONING
7.7. DNS SPOOFING ATTACKS
7.8. DOS AND DDOS ATTACK
7.9. GENERAL PREVENTION TECHNIQUES
7.10. INTRUSION DETEECTION AND PREVENTION SYSTEM (IDS/IPS)

# 7.1. WHAT IS NETWORK HACKING?
---
`NETWORK HACKIING`: is finding vulnerability in the net system to attack.
     ![[Pasted image 20240909060345.png]]
# 7.2. NETWORK FOOTPRINTING
---
- Network Recon process tools we use are:
        -nmap
        -ping: is the primiery testing connectivity way by sending ICMP.
        ![[Pasted image 20240909060903.png]]
                    ![[Pasted image 20240909062111.png]]
        ![[Pasted image 20240909061037.png]]
                     ![[Pasted image 20240909062144.png]]
	-traceroute: network diagnostic tool used to trace the path by checking the route taken and timetaken. 
                     ![[Pasted image 20240909062221.png]]
	    -arp
        -netstat:(net statistics) connected ip address we made routing tables, interface statistics and multicast memberships.![[Pasted image 20240909062847.png]]
![[Pasted image 20240909063130.png]]
   >> display active connections
   
![[Pasted image 20240909063230.png]]   
   >> listening ports
   
![[Pasted image 20240909063327.png]]   
   >> who create the connection with in it 
   
   -ss(socket statictics): faster than netstat
>> -t :tcp
>> -u :udp
>> -l :lisining
>> -p :process
     
# 7.3. NETWORK SNIFFIING
---
-`SNIFFING`: monitoring and capturing all packets passing through a given network using tools.
-`types`: 
A. passive sniffing: not alter, listening only, work with HUB devices.
B. active sniffing: altered, on switches.
-`tools`:
a.wireshark: passive sniffing tool, it will save it in the form of cap/ pcap files.
         : areas on { toolbar, packet list pane, packet detail pane, packet byte pane }
         : sessionlayer and presentation layers are no recognized.    
       ![[Pasted image 20240909074504.png]]

b.tcpdump: ![[Pasted image 20240909080752.png]]
c.tshark:   ![[Pasted image 20240909080235.png]]
-is a kind of wireshark and to analysie pakage that comes with wiresharek without userinterface.
d.microsoft message analyzer
e.network miner

# 7.4. NETWORK CAPTURES
---
  `ARP(ADDREE RESOLUTION PROTOCOL)`
![[Pasted image 20240909084442.png]]
                                            ![[Pasted image 20240909084202.png]]
`ARP COMMAND`:![[Pasted image 20240909084729.png]]
![[Pasted image 20240909084825.png]]


# 7.5. MAC ATTACK
---
`MAC FLOODING`: fake mac making then sending in mass to the swith.
- they first poison the mac table to pretending like the users doesn't exist.
![[Pasted image 20240909085615.png]]
 -network poisoning
![[Pasted image 20240909090032.png]]
-to erase that specific IP.


`MAC TABLE`:![[Pasted image 20240909090238.png]]
`PREVENTION`:![[Pasted image 20240909090327.png]]

# 7.6. ARP POISONING
---
![[Pasted image 20240909090814.png]]

![[Pasted image 20240909090905.png]]
1. IP forwared:
![[Pasted image 20240909095903.png]]
2. firewall disable
![[Pasted image 20240909095944.png]]
3. spoofing: knowing the user
![[Pasted image 20240909100119.png]]
-TO spofe POISONING:
![[Pasted image 20240909100739.png]]
`PREVENTION`:![[Pasted image 20240909101614.png]]

# 7.7. DNS SPOOFING ATTACKS
---
![[Pasted image 20240909103158.png]]
It works us:
![[Pasted image 20240909103242.png]]
![[Pasted image 20240909103957.png]]
# 7.8. DOS AND DDOS ATTACK
---
![[Pasted image 20240909104133.png]]
![[Pasted image 20240909104527.png]]
`PREVENTION WAYS`:
![[Pasted image 20240909105203.png]]
`GENERAL PREVENTION TECHNIQUES`:![[Pasted image 20240909105346.png]]

# 7.9. GENERAL PREVENTION TECHNIQUES
---

# 7.10. INTRUSION DETEECTION AND PREVENTION SYSTEM (IDS/IPS)
---

# Introduction To Networking
---
- Network: means when two or more objects share resources.
     - Computer networks: when two or more computer devices connected to each other and share resources.
             - computer: can be classified CLIENT  &  SERVER.
                       - Client: that request for resources.  
                       - Server: controls and access to resources also have higher RAM, CPU and STORAGE.
                            - ![[Pasted image 20240819121932.png]]
                            - Server Rack
                                 - Switch
                                 - Modem
                                 - Servers
                                 - Firewall
                                 - Display

- Need of Networks:
   ![[Pasted image 20240817201307.png]]

# Classification of Networks
---
 - ![[Pasted image 20240817201333.png]]
1. Geographical
     - LAN(local area network)
                    ![[Pasted image 20240819122418.png]]
           - ex: school, classroom or a single building.
           - that with home wifis that 10 peoples can use it.
           - it costes low.
     - MAN(metropolitian area network)
                        ![[Pasted image 20240817201642.png]]
                        - high cost.
                        - it uses fiber optics to connect this all.
    - WAN(Wide are network)
                    ![[Pasted image 20240819122932.png]]
                    -is a large area than a single city.
                    - example: internet.
                    - also called pan.
1. Component Roles
   - Peer-to-peer: 
![[Pasted image 20240817202015.png]]
                                               ![[Pasted image 20240819123610.png]]
   - Server based
![[Pasted image 20240817202049.png]]
                                             ![[Pasted image 20240819123637.png]]
 
 - Client based
![[Pasted image 20240817202130.png]]
                                            ![[Pasted image 20240817202150.png]]
# IP Address Technology
---
- DEFINATION![[Pasted image 20240817202245.png]]
- USAGE![[Pasted image 20240817202417.png]]
- TYPES:
![[Pasted image 20240817202449.png]]
     `IP4`: ![[Pasted image 20240817202518.png]]
           - While connecting to some networks:
                - DHCP: dynamically automatical
            - Manually: staticlly
    
- STRUCTURE:![[Pasted image 20240819124614.png]]
    -[To convert binary to decimal or visversa](https:/www.rapidtables.com/convert/number/binary-to-decimal.html)
    
  -   PARTS
     -`Network`: to identify the network.
     -`Host`: to identify the user.
PRIVATE AND PUBLIC IP ADDRESSES    
	- `private-IP`: address can be classified in 5 classes based on host and network part.![[Pasted image 20240819131115.png]]
                `GOVERNMENTS`: have 24bit spaces for host and 8 bits for networks.
                ![[Pasted image 20240819132237.png]]
                `MEDIUM COMPANIES`: have 16bits for hosts and 16bits for networks.
                 ![[Pasted image 20240819132312.png]]
                 `SMALL COMPANIES`: have 8bits for host and 24-bit of ntworks.
                 ![[Pasted image 20240819132333.png]]
                    - school , home and offices.
                 
                 `MULTICASTING(STREAMING)`:
                 `FUTURE USE(IETF RESEARCH)`:

- RESERVED IP addresses: when our device can not access the network.
    1. addresses beginning with 127. 
            - for loopback and internal.   
	2. IP address that is 0 has binary 0s in all the host part. 
            - for the network address.
	3. IP address that is 255 has binary 1 in all host bit positon.
            - for the broadcast.
    - EXAMPLES:![[Pasted image 20240819134724.png]]

   `IP6`:   ![[Pasted image 20240819135138.png]]
           - is used because their is limitation of ip4 and expensive.
           - ISP : ethiotelecom and safaricom.
           - peopels can't hack with the specific ip address cause of the static and dynamic form.
- to see private IP address use: `ipconfig` on windows and `ifconfig` on linux.
- to see public IP address use `google` on windows and `curl ifconfig.me` on linux.

NAT(Network Address Translation)
- translates public IP address to private IP address by using routers.
- this technology provides security by hiding internal IP addresses from external network(internet).

NETWORK DIVISION
- The Techniques are:
     1. Virtual Local Area Network(VLAN)
          -this means creating different virtual LAN's based on 1IP.
     2. Subnetting
          -ls segmenting the IP address based on subnet masks.
# Mac Address
---
-MAC(media access control address): from the manufacturer of the company. we can found it on the Network interface card[NIC].
-It is alphanumeric have 2 parts
   - Organizational Unique Id
   - Universally Administered Address
- flat name space of 48 bits (written in six octets in hex) 
   -![[Pasted image 20240819172344.png]]
   -![[Pasted image 20240819172404.png]]

# OSI Model
---
Open system Interconnection![[Pasted image 20240819173135.png]]
                                                ![[Pasted image 20240819173253.png]]
                    ![[Pasted image 20240819173328.png]]
*LAYER7: Protocol: http/https/ftp
*LAYER6: Protocol: SSL
*LAYER5: Protocol: RPC, NETBIOS
*LAYER4: Protocol: TCP,UDP
*LAYER3: Protocol: ICMP, ARP,NAT,IP 
*LAYER2: Protocol: PPP,NDP,CDP
*LAYER1: Protocol: RS-449
# Protocols 
---
-Network Protocol: are the rules and conventions that govern how data is transmitted and received over a network.
-Protocols: have their own name and abbreviation. 
# TCP/IP Model
---
![[Pasted image 20240819214805.png]]
# Networking Devices
---
- are used to connect different computers and create network.

Layer 1: Hub, repeater, networkcable(coaxial, twisted pair, fiberoptics)
    - firewall
Layer 2: switches
Layer 3: routeres modern wifi routers
-briges














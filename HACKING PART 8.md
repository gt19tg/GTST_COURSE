8.1. Anonymity
8.2. Methods of Anonymity
8.3. Proxy Servers
8.4. Virtual Private Networks
8.5. Onion Routing
8.6. DarkWeb

# 8.1. Anonymity
---
![[Pasted image 20240910231052.png]]
* ONLINE PRIVACY
# 8.2. Methods of Anonymity
---
![[Pasted image 20240910231554.png]]
# 8.3. Proxy Servers
---
- Used for security, privacy but most f the time it dependes.
![[Pasted image 20240910231715.png]]
Purpose of proxy server:
1. Anonymity
2. traffic filtering
3. Load balancing![[Pasted image 20240911221950.png]]
4. Caching![[Pasted image 20240911222118.png]]
Types based on its features:
1. Forward proxy : use cases(bypassing geo-blocks, hiding IP addresses)                        
                          ![[Pasted image 20240911223053.png]]
  2. Reverse proxy: front of web servers and forwards client requests to servers.
                          :use cases>> load balancing
                                  >> web acceleration
                                  >> application firewall/WAF
                            ![[Pasted image 20240911223924.png]]
3. Transparent proxy: proxy that does not modify requests or responses: use cases(caching, content filtering/ IDS-IPS)    
                             ![[Pasted image 20240911224240.png]]
4. Anonymous proxy: (basic anonymity without full stealth)
                                 ![[Pasted image 20240911224647.png]]

Proxy protocols: 
1. HTTP proxy:
-used for web browsing, content filtering and caching.

2. SOCKS proxy(SOCKS5) 
-handle any traffic(e.g. http, https, smtp and ftp).
`METHODS OF ANO...`
PROXY CHAIN:
-Is a chain of proxies
![[Pasted image 20240911231328.png]]
     - Types of proxy chains based on sequence:
         1. Dynamic chain
         2. Strict chain
         3. Round Robin chain
         4. Random chain
1. Dynamic chain: is the way we connect toe proxy servers.
              : if there is any server that is not working it will be skipped.
2. Strict chain: if one server is not working it will display error.
3. RRC: if 1 proxy is not working it will skip 
     : if it is all start again and check them.
4. random chain: choose randomly and chain in random

* find some proxy server to use
  a) google.com
  b) https://geonode.com/

T.O.R/The Onion Routing/Network
-is with node
![[Pasted image 20240912053858.png]]

![[Pasted image 20240912053956.png]]
- torgost
# 8.4. Virtual Private Networks
---
-VPN it incripts the IP address.
-VPN is the is server also a tunnel.![[Pasted image 20240912060217.png]]
-are encripted:![[Pasted image 20240912060406.png]]
-examples of vpn![[Pasted image 20240912060536.png]]
![[Pasted image 20240912060621.png]]

TYPES OF VPN:
A) SITE to SITE= router to router
                             ![[Pasted image 20240912061046.png]]
B)Remote Access VPN
C)SSL VPN
                             ![[Pasted image 20240912063111.png]]
TYPES OF VPN PROTOCOL:
1. OPEN VPN
2. IPSec /IKEv2: ipsec for incription or authuntication & IKEv2 tunnelling pourpose
![[Pasted image 20240912064550.png]]
3. Wire Guard

-MAC CHANGER:
1st turn off the interface you want to change.
![[Pasted image 20240912064826.png]]
2nd change the mac
![[Pasted image 20240912065428.png]]
- to see the statuse: ![[Pasted image 20240912065607.png]]
- ![[Pasted image 20240912065721.png]]
>> to change the mac address of different desktop models  

3rdturn it on:
![[Pasted image 20240912070014.png]]
to know the current, permanent and new mac address.
![[Pasted image 20240912070203.png]]

`INCOGNITO MODE`
-secured us from memory dump
`SECURE OS`
-Tails : by flash
-Whonix Os: only tor
-Qubes OS

`TEMPORARY MAIL`:
-[website]:[https://temp-mail.org/]
# 8.5. Onion Routing
# 8.6. Dark Web
>> .onion because they work on tor networkes.'tor': firrst created for miletary purpose.
>> dark web comes from the deep web or it is the small portion of it.
>>>> sudo apt install torbrowser-launcher: is to hidden  wiki







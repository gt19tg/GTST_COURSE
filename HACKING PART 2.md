s2Day1_info.md
# RECONNAISSANCE [INFORMATION GATHERING]
2.1. INTRODUCTION TO PENETRATION TESTING
2.2. PRE-ENGAGEMENT STEP
2.3. WHAT IS INFORMATION GATHERING/FOOTPRINTING/
2.4. WHAT INFORMATION WE GATHER
2.5. TYPES OF INFORMATION GATHERING
2.6. HOW WE GATHER INFORMATION
2.7. REVERSE IMAGE SEARCH
2.8. GOOGLE HAKING DATABASE


## Reconnaissance: 
   -  focuses on broad, high-level info about the target.
   - ![[Pasted image 20240901073222.png]]
# 2.1. INTRODUCTION TO PENETRATION TESTING
--- 


![[Pasted image 20240901065424.png]]
-Red team is must for the blue team.
# 2.2. PRE-ENGAGEMENT STEP
---
-gives us full permission and understanding about system you are doing to Test on.
![[Pasted image 20240901065708.png]]
1. SCOPING QUESTIONNAIR
     - help us to gather detail info about the target envi, what assets will be tested, the type of testing required, restrictions and timelines.
     - eg: black-box, white-box
     - the questionnaire must ask the m abut the cyber security services we  are giving. 
2. PRE-ENGAGEMENT MEETING
     - discuss the details gathered from the scoping questionnaire and clarify any uncertainties.
     - ![[Pasted image 20240901070932.png]]
     - ![[Pasted image 20240901071124.png]]
     - REQUIRES ==AGREEMENTS==
          -  ![[Pasted image 20240901071316.png]]

3. KICK-OFF MEETING
     - discusses the engagement schedule, communication protocols, escalation processes and final testing approach(retest/no-retest).
# 2.3. WHAT IS INFORMATION GATHERING/FOOTPRINTING/
---
- it also called `recon`.
- footprinting = footstep + printing(logging).
- is collecting data about some network/host/system.
- `TO FIND VULNERABLE`
TYPES OF RECON
1. ACTIVE RECON
  - Gathering info directli by contacting that person.
  - is `ILLEEGAL!!!` in cybersecurity.
2. PASSIVE RECON
  - 3rd party or checking public sources.
     
# 2.4. WHAT INFORMATION WE GATHER
---
`TYPES OF INFO`
-host, network, person/org/application
# 2.5. TYPES OF INFORMATION GATHERING
---

1. HOST
     A. WEBSITES:
         *  IP address
         * Development frameworks
             * tech used and versions
         * name
         * DNS info
         * subdomains, assets, contents
# 2.6. HOW WE GATHER INFORMATION
---
    
#### TO GET IP 
     -`ACTIVILY`: 
         * Ping 'web link'
         * nslookup 'web link'
         * host 'website link'
     -`PASSIVE`:
         * www.nsllookup.io
#### TO GET DEVELOPMENT FRAMEWORKS
     - `simple browser extension`
        -wapplyzer "wapplyzer for chrome"
        -Builtwith
     - `terminal tool`
        -whatweb
#### TO GET THE NAME

#### TO GET THE DNS info
      - whois
      - dig
    B. Computers/Phone:`scanning and enumeration`
     ![[Pasted image 20240827151520.png]]
    C. Networks:`network penetration testing`
      ![[Pasted image 20240827155018.png]]
   D. Personal Informations: 
      ![[Pasted image 20240827155459.png]]
      - OSINT ( open source intelligence )
         -getting names by phone number[https://www.truecaller.com/]
         -getting social medias addresses: [google,bing,yahoo]
         -ex: sherlock
         -getting physical address
         -IP geolocation[https://www.iplocation.net]
    E. Applications/softwares
         -which programming langu
         -which framework
         -source codes
         -their logic and function
# 2.7. REVERSE IMAGE SEARCH
---
-Reverse image search
- [https://tineye.com/](https://tineye.com/)
- [https://www.labnol.org/reverse/](https://www.labnol.org/reverse/)
- [https://images.google.com/](https://images.google.com/)**



# 2.8. GOOGLE HAKING DATABASE
---
- also called `gooogle dorking`.
- ### Basic Operators
   * (+): inclusion
   * ( - ): exclude
   * (" "): exact term 
   * ( * ):any word(wild card)
   * ( | ): or
- #### ADVANCED OPERATORS
   - intitle- (intitle:)-word/phrase
   - inurl- (inurl:)-for linkes specifically
   - filetype-("text/book")filetype:pdf ,xml
   - intext-(intext:"xxx")
- #### MIXING OPERATORS
  - ![[Pasted image 20240827173914.png]]

- GHD: google hacking Database[**[https://www.exploit-db.com/google-hacking-database](https://www.exploit-db.com/google-hacking-database)**]











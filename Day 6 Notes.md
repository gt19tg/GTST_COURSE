# Final Topic on Linux

6.1. Script Installation
6.2. Package Installation
6.3. Package Installation Common Errors
6.4. HELP ON LINUX
6.5. LINUX SERVICES
6.6. SYMBOLIC LINKING
6.7. ALIAS
6.8. TMUX
6.9. WGET
6.10.  FIND
# D. Script Installation
---
- Script: file or something that found in an written form or tangible form.
- this scripts can be download and use only by using links from github uploads.
- Syntax: "git clone <link_of_the_script_from_github>".
- one of the git feature is "clone".
#### Script Modules
- to run the script we need to download the dependencies also called modules/ libraries.
- scripts are made up of programming languages
     1. python-> pip install < module name> , {pip install -r requirements.txt}: if their is any requirement files
     2. Go-> go install < modulename >
         - sudo mv filename_/usr/bin: to move the file otherwise it doesn't open
     3. Ruby-> gem install< modulename >
# E. Package Installation Common Errors
---
![[Pasted image 20240803205703.png]]
# F. HELP ON LINUX
---
- man(manual) < command to know>: it gives detail info of the command.
-  < your command> -help, -h, --help: it get options.
# G. LINUX SERVICES
--- 
- linux processes:- are created numbered instances of running programs.
- ps -A:-running process on the machine
- ps:-all running process n the shell
- ps-u username:-view users process
- PID: process id is the id given for the tools that are being used on the machine
- kill {options}{pid}: options are 31 in number
     only this 3 options are essential:
         1. kill -19PID -> to stop the process
         2. kill -18PID -> to resume the process immediately
         3. kill -9PID -> to stop a process immediately
- top & htop: instead of using ps it is simple to use htop.
- foreground /background: & or control Z
                     : to get it back
- to stop process control C
- ct .dev/null 2> /dev/null: 2 for studerr, 1 for stout 
# H. SYMBOLIC LINKING
---
- used to create shortcuts from file to some pre-existed file or folder
- Syntax: ln -s source_filePATH myfilename 
- works for files and folders

# I. ALIAS
---
- works for commands not for files or folders
- it worked to give a name to bunch of commands.
- for the alias to fix or made it work permanently we use Zsh = ~/.zshrc, bash = ~/.bashrc, fish = ~/config/fish/config.fish
 
# J. TMUX
---

# K. WGET
---
- Used to download files from websites/servers
- copy the URL
# L. FIND
---
- to search for files/folders/musics/videos
- Syntax: find(searchpath)(options)(search word)
- find/-name"linux": to find name
- find/home-perm777: to find permission
- find -type f | find-type d:
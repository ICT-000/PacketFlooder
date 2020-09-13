# PacketFlooder
Floods Minecraft Server with packets (CPS, PPS, AND NULLPINGS)

## What is it about?
Sends multiple packets to a minecraft proxy simulating high traffic

## Installation

You just have to **git clone** the repository and put some proxies onto **socks5.txt** and **socks4.txt**

* `git clone https://github.com/GhostyCeh/PacketFlooder`
* `cd PacketFlooder`
* `sudo pip3 install PySocks`
* `sudo python3 Flooder.py`


## Available Methods
* `DemonShredder - Sends PING packets Continously to the IP:PORT`
* `HadesDestroyer - Sends Connection Packets (CPS) with an static nickname (For Simulating Traffic, NOT BOTTING)`
* `NullPing - Sends invalid packets (trash, can be fixed using FlameCord)`

## Execute the script -
`python3 Flooder.py` - Input data manually

`python3 Flooder.py -host IP -p PORT  -threads Threads_Number -type 4/5 --amplification 100  -pFile Proxies_File -m Method (1/2/3)` - Input data with in-command-arguments.

You can enable print option in Flooder.py, i didn't set it as default due to less perfomance if printing each request!

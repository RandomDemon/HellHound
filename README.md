# IP Adress Info Grabber
## Info
This script takes an IP address you provide, and finds the:
* City of origin
* State/Province of origin
* Country of origin
* ISP (Internet Service Provider) for the address
If you are trying to find the information of a website, you must first enter your command line and type
``` ping (Website or server address) ```
For example, I'll try to ping the popular Minecraft server Hypixel:
``` ping mc.hypixel.net ```
And the output would be:
``` Pinging mt.mc.production.hypixel.io [209.222.115.31] with 32 bytes of data: ```\
This would be followed by the information of the packets sent to the server. The only information here that matters is that IPv4 address (209.222...). This is what you would paste into the application.\
**(This may vary depending on Operating System)**
## Installation
* ``` pip install PySimpleGUI ```
* Download this repo
* Run main.py
* Follow the instructions under the **Info** section

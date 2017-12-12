#!/usr/bin.python3
import os
print("		|                                                                              |")
print("		|                          I love Security and Haking.                         |")
print("		|______________________________________________________________________________|")
print("		|                                                                              |")
print("		|                                                                              |")
print("		|                                                                              |")
print("		|                 User Name:          [   brenss    ]                          |")
print("		|                                                                              |")
print("		|                 Password:           [               ]                        |")
print("		|                                                                              |")
print("		|                                                                              |")
print("		|                                                                              |") 
print("         |                                                                              |")
print("		| My youtube channel: https://www.youtube.com/channel/UCuVdwrJjf9kbWf-DGtrYX6A |")	                                                                                  
print("		|                                                                              |")
print("		|                                   [ OK ]                                     |")
print("		|______________________________________________________________________________|")


print(" \n 1) UPDATE\n\n 3) VPN\n\n 4) gufw\n\n 2) wine\n\n 22) Browser chromium\n\n 99) Exit\n\n 5) tor\n")
def update():
    import os
    os.system('sudo apt-get update')
def wine():
    import os
    os.system('sudo apt-get install -y wine')
def vpn():
    import os
    os.system('sudo apt-get -y install  network-manager-openvpn network-manager-openvpn-gnome  network-manager-pptp network-manager-pptp-gnome  network-manager-strongswan network-manager-vpnc  network-manager-vpnc-gnome')
def gufw():
    import os
    os.system('sudo apt-get -y install gufw')
def exit():
    import os
    os.system('exit')
def Browser():
    import os
    os.system('sudo apt-get -y install chromium') 
def tor():
    import os
    os.system('sudo apt-get -y install tor')   
while True:
    nmbers=input('Enter a number  :')
    if nmbers=='1':
       update()
    elif nmbers=='2':
         wine()
    elif nmbers=='22':  
         Browser
    elif nmbers=='3':   
         vpn()
    elif nmbers=='4':
         gufw()
    elif nmbers=='5':
         tor()
    elif nmbers=='99':
     break   
    else:
         print('intr yur nambr')

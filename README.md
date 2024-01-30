# MACchanger

MACchanger - is a program that helps us to change device MAC address for protecting user privacy.

Before running program this additional thing needed (2nd is optional)

* Linux
* USB WiFi adapter (optional)

## Part 1

Find name of the interface that you want to change MAC address

For this run :

- ```bash 
   sudo apt install python3 python3-pip -y 
   sudo git clone https://github.com/poseydonianexe/Macchanger.git
   cd Macchanger/
   sudo chmod +x macchanger.py 
   sudo ifconfig
  ```
- Then copy name of the interface

## One command mode (normal mode)

1. Execute the following command in the terminal:

   ```bash
    sudo ./macchanger.py -i <interface> -m <mac address>
   ```

2. Then you see this text:
   ```text
   [+] Old MAC :;  <your old mac address>
   [+] New MAC ::  <your new mac address>
   [+] MAC address changed

   ```

## Manual Mode

1. Execute the following command in the terminal :
   ```bash
   sudo ./macchanger.py --manual-mode 1
   ```
2. Then you see the list of interfaces active in your computer.
3. Select one for changing MAC address
4. Enter the interface name then add MAC address.
   ```text
   [+] New MAC ::  <your new MAC address>
   [+] MAC address changed

   ```
5. After all MAC address alredy cahged

## Credits

Poseydonian.exe : [Instagram](https://www.instagram.com/poseydonian.exe/)



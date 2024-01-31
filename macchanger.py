#!/usr/bin/env python

import optparse
import re
import subprocess

from colorama import Fore, Style
try:
    try:
        def get_options():
            parser = optparse.OptionParser()
            parser.add_option("-i", "--interface", dest="interface", help=" Enter the interface")
            parser.add_option("-m", "--new-mac", dest="mac", help=" Enter the New Mac address")
            parser.add_option("--manual-mode", dest="manual_mode", help="Enables manuall mode")
            (options, arguments) = parser.parse_args()

            if not options.interface and options.manual_mode == 1:
                print(Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + " Please enter the interface" + Style.RESET_ALL)
            elif not options.mac and options.manual_mode == 1:
                print(Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + "Please neter the MAC address" + Style.RESET_ALL)

            return options


        def change_mac(options):
            interface = options.interface
            mac = options.mac
            try:
                ifconfig_output2 = subprocess.check_output(["sudo", "ifconfig", interface])


            except subprocess.CalledProcessError:
                print(Fore.RED + " [-] Failed to change MAS address or you entered same MAC address")
                print(" [-] MAC address not changed" + Style.RESET_ALL)
                print(
                    Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + " Please enter the real interface"
                    + Style.RESET_ALL)
                quit()

            subprocess.call(["sudo", "ifconfig", interface, "down"])
            subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
            subprocess.call(["sudo", "ifconfig", interface, "up"])

            print(Fore.LIGHTYELLOW_EX + " [+] " + Fore.LIGHTWHITE_EX + "New MAC :: " + Fore.GREEN + mac + Style.RESET_ALL)
            print(Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + "MAC address changed")


        def get_mac(interface):
            ifconfig_result = str(subprocess.check_output(["sudo", "ifconfig", get_options().interface]))
            old_mac = re.search(r"..:..:..:..:..:..", ifconfig_result)
            if old_mac:
                return old_mac.group(0)

            else:
                print(
                    Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + "Please enter network interface that actually have MAC address")


        def manual_mode():
            print("dsds")
            subprocess.call(["sudo", "ifconfig", "-s"])
            interface = input(Fore.CYAN + Style.BRIGHT + "Enter the interface :: " + Style.RESET_ALL)
            mac = input(Fore.CYAN + "Enter new MAC address :: " + Style.RESET_ALL)

            old_mac = ""

            subprocess.call(["sudo", "ifconfig", interface, "down"])
            subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
            subprocess.call(["sudo", "ifconfig", interface, "up"])
            if old_mac != mac:
                print(
                    Fore.LIGHTYELLOW_EX + " [+] " + Fore.LIGHTWHITE_EX + "New MAC :: " + Fore.GREEN + mac + Style.RESET_ALL)
                print(Fore.LIGHTYELLOW_EX + " [*] " + Fore.LIGHTWHITE_EX + "MAC address changed")

            else:
                print(Fore.RED + " [-] Failed to change MAS address or you entered same MAC address")
                print(" [+] MAC address not changed" + Style.RESET_ALL)


        if get_options().manual_mode == "1":
            manual_mode()
        else:
            change_mac(get_options())

    except TypeError:
        subprocess.call(["python", "macchanger.py", "--help"])
except KeyboardInterrupt:
    print(Fore.YELLOW + "\n  [***] Quitting" + Style.RESET_ALL)
    quit()

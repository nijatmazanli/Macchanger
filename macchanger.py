#!/usr/bin/env python

import subprocess
import optparse
import re


def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" Enter the interface")
    parser.add_option("-m", "--new-mac", dest="mac", help=" Enter the New Mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        print(" [*] Please enter the interface")
    elif not options.mac:
        print("[*] Please neter the MAC address")

    return options


def change_mac(options):
    interface = options.interface
    mac = options.mac

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])


def get_mac(interface):
    ifconfig_result = str(subprocess.check_output(["sudo", "ifconfig", get_options().interface]))
    old_mac = re.search(r"..:..:..:..:..:..", ifconfig_result)
    if old_mac:
        return old_mac.group(0)

    else:
        print(" [*] Please enter network interface that actually have MAC address")


old_mac = get_mac(get_options().interface)
change_mac(get_options())
new_mac = get_mac(get_options().interface)
print(" [+] Old MAC :; ", old_mac)
if old_mac != new_mac:
    print(" [+] New MAC :: ", new_mac)
    print(" [+] MAC address changed")

else:
    print(" [-] Failed to change MAS address or you entered same MAC address")
    print(" [+] MAC address not changed")


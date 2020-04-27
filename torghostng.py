#!/usr/bin/python3

import argparse
from time import sleep
from json import JSONDecodeError, loads
from sys import argv, exit
from subprocess import getoutput
from os import geteuid, system, path, name

try:
    from torngconf.theme import *
except ModuleNotFoundError:
    print("TorghostNG is lacking its needed files. Reinstall TorghostNG from Github pls")
    exit()

SLEEP_TIME = 1.0
VERSION = "1.3"

def the_argparse(language=English):
        parser = argparse.ArgumentParser(usage="torghostng [-h] -s|-x|-id|-r|-m|-c|-l|--list")
        parser._optionals.title = language.options
        parser.add_argument("-s","--start", help=language.start_help, action="store_true")
        parser.add_argument("-x", "--stop", help=language.stop_help, action="store_true")
        parser.add_argument("-r", "--renew", help=language.circuit_help, action="store_true")
        parser.add_argument("-id", help=language.id_help, metavar=language.country_id, type=str)
        parser.add_argument("-mac", help=language.changemac_help, metavar="INTERFACE", type=str)
        parser.add_argument("-c","--checkip", help=language.checkip_help, action="store_true")
        parser.add_argument("--dns", help=language.dns_help, action="store_true")
        parser.add_argument("-l","--language", help=language.language_help, action="store_true")
        parser.add_argument("--list", help=language.language_list_help, action="store_true")
        parser.add_argument("-u", "--update", help=language.update_help, action="store_true")
        parser.add_argument("--nodelay", help=language.no_delay_help, action="store_true")

        if len(argv) == 1:
            banner()
            parser.print_help()
            exit()

        return parser.parse_args()


if (path.isfile('/usr/bin/upgradepkg') == True) or (path.isfile('/usr/bin/torngconf/langconf.txt') == False):
    LANGCONF = 'torngconf/langconf.txt'
else:
    LANGCONF = '/usr/bin/torngconf/langconf.txt'

if path.isfile('/usr/bin/apt') == True:
    TOR_USER = 'debian-tor'
else:
    TOR_USER = 'tor'

Torrc = '/etc/tor/torngrc'
resolv = '/etc/resolv.conf'
Sysctl = '/etc/sysctl.conf'

TOR_UID = getoutput('id -ur {}'.format(TOR_USER))

FIX_DNS = """nameserver 1.1.1.1
nameserver 1.0.0.1
nameserver 2606:4700:4700::1111
nameserver 2606:4700:4700::1001"""

DISABLE_IPv6 = """net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1"""

resolvConfig = 'nameserver 127.0.0.1'

TorrcConfig = """VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 5353
ControlPort 9051
RunAsDaemon 1"""

TorrcConfig_exitnode = """VirtualAddrNetwork 10.0.0.0/10
AutomapHostsOnResolve 1
TransPort 9040
DNSPort 5353
ControlPort 9051
RunAsDaemon 1
ExitNodes {%s}"""

iptables_rules = """NON_TOR="192.168.1.0/24 192.168.0.0/24"
TOR_UID={}
TRANS_PORT="9040"

iptables -F
iptables -t nat -F

iptables -t nat -A OUTPUT -m owner --uid-owner $TOR_UID -j RETURN
iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 5353
for NET in $NON_TOR 127.0.0.0/9 127.128.0.0/10; do
 iptables -t nat -A OUTPUT -d $NET -j RETURN
done
iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports $TRANS_PORT

iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
for NET in $NON_TOR 127.0.0.0/8; do
 iptables -A OUTPUT -d $NET -j ACCEPT
done
iptables -A OUTPUT -m owner --uid-owner $TOR_UID -j ACCEPT
iptables -A OUTPUT -j REJECT

iptables -A FORWARD -m string --string "BitTorrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "BitTorrent protocol" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "peer_id=" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string ".torrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "announce.php?passkey=" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "torrent" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "announce" --algo bm --to 65535 -j DROP
iptables -A FORWARD -m string --string "info_hash" --algo bm --to 65535 -j DROP""".format(TOR_UID)

IpFlush = """iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X"""

update_commands = """cd ~ && rm -rf TorghostNG
git clone https://github.com/gitkern3l/TorghostNG
cd TorghostNG
sudo python3 install.py && sudo python3 install.py"""

def banner():
    print(the_banner)
    print(language.description)
    
def check_lang():
    try:
        if path.isfile(LANGCONF) == True:
            with open(LANGCONF) as file_lang:
                language = eval(file_lang.readline())

                file_lang.close()

                print(language.applying_language, end='', flush=True)
                print(language.done)

                return language
        else:
            language = choose_lang()
            return language
        
    except KeyboardInterrupt:
        print()
        exit()
    except (NameError, SyntaxError, AttributeError):
        language = choose_lang()
        return language
    except FileNotFoundError:
        print("TorghostNG is lacking its needed files. Reinstall TorghostNG from Github pls")
        exit()

def choose_lang(language=English):
    try:
        with open(LANGCONF, mode="w") as file_lang:            
            print(language.language_list)
            choice = int(input(language.choose_your_lang))
            
            if choice == 1:
                print(English.applying_language)
                file_lang.write("English")
                language = English
    
            
            elif choice == 2:
                print(Vietnamese.applying_language)
                file_lang.write("Vietnamese")
                language = Vietnamese

            else:
                print()
                print(language.invalid_choice)
                choose_lang()

            file_lang.close()
            return language

    except KeyboardInterrupt:
        print()
        exit()

def check_windows_check_root():
    if name == "nt":
        print(English.sorry_windows)
        exit()
    
    if geteuid() != 0:
        print(language.root_please)
        exit()

def check_update():
    try:
        print(language.checking_update, end='', flush=True)
        version = getoutput('curl -s --max-time 60 https://raw.githubusercontent.com/gitkern3l/TorghostNG/master/torngconf/Version')
        sleep(SLEEP_TIME)
        print(language.done)

        if (version != VERSION) == True:
            print(language.outofdate)
            choice = str(input(language.wanna_update))
            
            if choice[0].upper() == "Y":
                print(language.updating.format(version))
                system(update_commands)
                exit()
                   
        else:
            print(language.uptodate)
    
    except KeyboardInterrupt:
        print()
        exit()

def check_tor(status):
    try:
        print(language.checking_tor, end='', flush=True)
        sleep(SLEEP_TIME)
        tor_status = loads(getoutput("curl -s --max-time 60 https://check.torproject.org/api/ip"))
        print(language.done)
        
        if tor_status['IsTor'] == False:
            if status == "failed":
                print(language.tor_failed)
                stop_connecting()
                
            elif status == "stopped":
                print(language.tor_disconnected)
            
        else:
            print(language.tor_success)

        check_ip()

    except KeyboardInterrupt:
        print()
        exit()

    except JSONDecodeError:
        print()
        sleep(1)
        check_tor(status)
            
def check_ip():
    try:
        print(language.checking_ip, end='', flush=True)
        sleep(SLEEP_TIME)
        ipv4_address = getoutput('curl -s --max-time 60 https://api.ipify.org')
        ipv6_address = getoutput('curl -s --max-time 60 https://api6.ipify.org')
        print(language.done)
        
        print(language.your_ip.format('IPv4') + color.BOLD + ipv4_address + color.END)
        
        if ipv6_address != ipv4_address:
            print(language.your_ip.format('IPv6') + color.BOLD + ipv6_address + color.END)

    except KeyboardInterrupt:
        print()
        exit()

def start_connecting(id=None):
    try:
        print(icon.process + ' ' + language.start_help)
        
        # Disable IPv6
        if DISABLE_IPv6 == open(Sysctl).read():
            print(language.ipv6_alreay_disabled)
            
        else:
            print(language.disable_ipv6_info)

            system('sudo cp {} /etc/sysctl.conf.backup'.format(Sysctl))
            print(language.disabling_ipv6, end='', flush=True)
            
            with open(Sysctl, mode='w') as file_sysctl:
                file_sysctl.write(DISABLE_IPv6)
                file_sysctl.close()

            sleep(SLEEP_TIME)
            print(language.done)

        getoutput('sudo sysctl -p')

        # Configure Torrc
        if id != None: # Check for exit node
            torrconfig = TorrcConfig_exitnode %(id)
            print(language.id_tip)
        else:
            torrconfig = TorrcConfig


        if (path.isfile(Torrc)) and (torrconfig == open(Torrc).read()):
            print(language.already_configured.format('TorghostNG Torrc'))
            
        else:
            print(language.configuring.format('TorghostNG Torrc'), end='', flush=True)

            with open(Torrc, mode='w') as file_torrc:
                file_torrc.write(torrconfig)
                file_torrc.close()
                
            sleep(SLEEP_TIME)
            print(language.done)

        # Configure DNS resolv.conf
        if resolvConfig == open(resolv).read():
            print(language.already_configured.format('DNS resolv.conf'))
            
        else:
            system("cp {} /etc/resolv.conf.backup".format(resolv))

            with open(resolv, mode='w') as file_resolv:
                print(language.configuring.format('DNS resolv.conf'), end='', flush=True)
                file_resolv.write(resolvConfig)
                file_resolv.close()
                sleep(SLEEP_TIME)
                print(language.done)

        # Stop and start new tor service
        print(language.stopping_tor, end='', flush=True)
        system('systemctl stop tor')
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)
        
        print(language.starting_tor, end='', flush=True)
        system('sudo -u {0} tor -f {1} > /dev/null'.format(TOR_USER, Torrc))
        sleep(SLEEP_TIME)
        print(language.done)

        # Show some info
        print(language.iptables_info)
        print(language.block_bittorrent)

        # Configure iptables
        print(language.setting_iptables, end='', flush=True)
        system(iptables_rules)
        sleep(SLEEP_TIME)
        print(language.done)
        
        check_tor('failed') # Check tor connection

        print(language.dns_tip) # Show some info

    except KeyboardInterrupt:
        print()
        exit()

def stop_connecting():
    try:
        print(icon.process + ' ' + language.stop_help)

        # Restore DNS resolv.conf configuration
        if path.isfile('/etc/resolv.conf.backup') == True:
            print(language.restoring_configuration.format('DNS resolv.conf'), end='', flush=True)

            system('mv /etc/resolv.conf.backup {}'.format(resolv))

            sleep(SLEEP_TIME)
            print(language.done)

        # Restore IPv6 configuration
        if path.isfile('/etc/sysctl.conf.backup') == True:
            print(language.restoring_configuration.format('IPv6'), end='', flush=True)

            system('mv /etc/sysctl.conf.backup {}'.format(Sysctl))
            system('sudo sysctl -p')

            sleep(SLEEP_TIME)
            print(language.done)

        # Reset iptables configuration
        print(language.flushing_iptables, end='', flush=True)
        system(IpFlush)
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)

        # Restart NetworkManager
        print(language.restarting_network, end='', flush=True)
        system('systemctl restart --now NetworkManager')
        sleep(8)
        print(language.done)
        
        check_tor('stopped') # Check tor connection

        print(language.dns_tip) # Show some info

    except KeyboardInterrupt:
        print()
        exit()

def change_tor_circuit():
    try:
        print(language.changing_tor_circuit, end='', flush=True)

        tor_status = loads(getoutput("curl -s --max-time 60 https://check.torproject.org/api/ip"))
        
        if tor_status['IsTor'] == True:
            system('pidof tor | xargs sudo kill -HUP')
            sleep(SLEEP_TIME)
            print(language.done)
            check_tor('stopped')
            
        else:
            print()
            start_connecting()
            
    except KeyboardInterrupt:
        print()
        exit()

def changemac(interface):
    try:
        print(language.changing_mac)
        
        i = getoutput('ifconfig {} down'.format(interface))

        if "ERROR" in i:
            print(language.interface_error.format(interface))
        else:
            system('macchanger -r {}'.format(interface))
            system('ifconfig {} up'.format(interface))
            sleep(SLEEP_TIME)
            print(language.mac_changed)
            
        print(language.ifconfig_tip)
        
    except KeyboardInterrupt:
        print()
        exit()

def fix_dns():
    try:
        print(language.fixing_dns, end='', flush=True)
        
        with open(resolv, mode='w') as file:
            file.write(FIX_DNS)
            file.close()
            
        sleep(SLEEP_TIME)
        print(language.done)
        
    except KeyboardInterrupt:
        print()
        exit()

if __name__ == "__main__":
    language = check_lang()
    check_windows_check_root()
    args = the_argparse(language)

    banner()
    print()
    
    if args.nodelay == True: SLEEP_TIME = 0

    if args.list == True: print(language.language_list)

    if args.language == True: language = choose_lang(language)
        
    if args.update == True: check_update()

    if args.dns == True: fix_dns()
        
    if args.checkip == True: check_tor('stopped')
        
    your_interface = args.mac
    if your_interface != None: changemac(your_interface)

    if args.start == True:
        start_connecting()
        exit()

    if args.stop == True:
        stop_connecting()
        exit()
        
    the_id = args.id
    if the_id:
        start_connecting(the_id)
        exit()
        
    if args.renew == True: change_tor_circuit()

print(language.video_tutorials)

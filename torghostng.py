#!/usr/bin/python3

import argparse
from time import sleep
from sys import argv, exit
from subprocess import getoutput
from torngconf.theme import *
from os import geteuid, system, path, name

SLEEP_TIME = 1.0
VERSION = "1.0"


def the_argparse(language=English):
        parser = argparse.ArgumentParser(usage="torghostng [-h] -s|-x|-id|-m|-c|-l|--list", add_help=False)
        parser._optionals.title = language.options
        parser.add_argument("-h","--help", help=language.help_help, action="help", default=argparse.SUPPRESS)
        parser.add_argument("-s","--start", help=language.start_help, action="store_true")
        parser.add_argument("-x", "--stop", help=language.stop_help, action="store_true")
        parser.add_argument("-id", help=language.id_help, metavar=language.country_id, type=str)
        parser.add_argument("-mac", help=language.changemac_help, metavar="INTERFACE", type=str)
        parser.add_argument("-c","--checkip", help=language.checkip_help, action="store_true")
        parser.add_argument("--nodelay", help=language.no_delay_help, action="store_true")
        parser.add_argument("-l","--language", help=language.language_help, action="store_true")
        parser.add_argument("--list", help=language.language_list_help, action="store_true")
        parser.add_argument("-u", "--update", help=language.update_help, action="store_true")
        parser.add_argument("--dns", help=language.dns_help, action="store_true")

        if len(argv) == 1:
            banner()
            parser.print_help()
            exit()

        return parser.parse_args()


if path.isfile('/usr/bin/upgradepkg') == True:
    LANGCONF = 'torngconf/langconf.txt'
    update_commands = """sudo git pull"""
else:
    LANGCONF = '/usr/bin/torngconf/langconf.txt'
    update_commands = """cd ~
sudo git clone https://github.com/gitkern3l/TorghostNG
cd TorghostNG && sudo python3 install.py"""


if path.isfile('/usr/bin/apt') == True:
    TOR_USER = 'debian-tor'
else:
    TOR_USER = 'tor'


TOR_UID = getoutput('id -ur {}'.format(TOR_USER))

FIX_DNS = """nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 2001:4860:4860::8888
nameserver 2001:4860:4860::8844"""

Torrc = '/etc/tor/torngrc'
resolv = '/etc/resolv.conf'

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
iptables -A OUTPUT -j REJECT""".format(TOR_UID)

IpFlush = """iptables -P INPUT ACCEPT
iptables -P FORWARD ACCEPT
iptables -P OUTPUT ACCEPT
iptables -t nat -F
iptables -t mangle -F
iptables -F
iptables -X"""

update_commands = """cd ~
sudo git clone https://github.com/gitkern3l/TorghostNG
cd TorghostNG && sudo python3 install.py"""

def banner():
    print(the_banner)
    print(language.description)

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
        version = getoutput('curl -s --max-time 10 https://raw.githubusercontent.com/gitkern3l/TorghostNG/master/torngconf/Version')
        sleep(SLEEP_TIME)
        print(language.done)

        if (version != VERSION) == True:
            print(language.outofdate)
            choice = str(input(language.wanna_update))
            
            if choice[0].upper() == "Y":
                print(language.updating.format(version))
                system(update_commands)
                print(language.uptodate)
                exit()
                   
        else:
            print(language.uptodate)
    
    except KeyboardInterrupt:
        print()
        exit()
                

def check_tor(status):
    try:
        print(language.checking_tor, end='', flush=True)
        sleep(5)
        tor_status = getoutput("curl -s --max-time 20 https://check.torproject.org | grep Congratulations")
        sleep(SLEEP_TIME)
        print(language.done)
        
        if 'Congratulations' in tor_status:
            print(language.tor_success)
            check_ip()
            
        else:
            if status == "failed":
                print(language.tor_failed)
                check_ip()
                stop_connecting()
                
            elif status == "stopped":
                print(language.tor_disconnected)
                check_ip()

    except KeyboardInterrupt:
        print()
        exit()
            
            
def check_ip():
    try:
        print(language.checking_ip, end='', flush=True)
        ip_address = getoutput('curl -s --max-time 10 https://fathomless-tor-66488.herokuapp.com/ip')
        sleep(SLEEP_TIME)
        print(language.done)
        print(language.your_ip + color.BOLD + ip_address + color.END)

    except KeyboardInterrupt:
        print()
        exit()


def check_lang():
    try:
        if path.isfile(LANGCONF) == True:
            with open(LANGCONF) as file_lang:
                lang = eval(file_lang.readline())

                file_lang.close()

                print(lang.applying_language, end='', flush=True)
                sleep(SLEEP_TIME)
                print(lang.done)

                return lang
        else:
            lang = choose_lang()
            return lang
        
    except KeyboardInterrupt:
        print()
        exit()
    except (NameError, SyntaxError):
        lang = choose_lang()
        return lang
    except FileNotFoundError:
        print("TorghostNG is lacking its needed files. Reinstall TorghostNG pls")
        exit()


def choose_lang(language=English):
    try:
        with open(LANGCONF, mode="w") as file_lang:
            file_lang.truncate(0)
            
            print(language.language_list)
            choice = int(input(language.choose_your_lang))
            
            if choice == 1:
                print(English.applying_language, end='', flush=True)
                file_lang.write("English")
                sleep(SLEEP_TIME)
                print(English.done)
                print(English.current_language + "English")
                return English
            
            if choice == 2:
                print(Vietnamese.applying_language, end='', flush=True)
                file_lang.write("Vietnamese")
                sleep(SLEEP_TIME)
                print(Vietnamese.done)
                print(Vietnamese.current_language + "Vietnamese")
                return Vietnamese

            else:
                print(language.invalid_choice)
                choose_lang()

            file_lang.close()

    except KeyboardInterrupt:
        print()
        exit()


def try_again():
    try:
        choice = str(input(language.try_again))
            
        if choice[0].upper() =="Y":
            system('clear')
            sleep(SLEEP_TIME)
            start_connecting()
                
        elif choice[0].upper() =="N":
            exit()
            
        else:
            print(language.invalid_choice)
        
    except KeyboardInterrupt:
        print()
        exit()


def start_connecting(id=None):
    try:
        print(language.connecting_tor)
        
        if id != None:
            torrconfig = TorrcConfig_exitnode %(id)
            print(language.id_tip)
        else:
            torrconfig = TorrcConfig
        
        sleep(SLEEP_TIME)
        
        if (path.isfile(Torrc)) and (torrconfig == open(Torrc).read()):
            print(language.torrc_already_configured)
            
        else:
            with open(Torrc, mode='w') as file_torrc:
                print(language.configuring_torrc, end='', flush=True)
                file_torrc.write(torrconfig)
                sleep(SLEEP_TIME)
                print(language.done)
                file_torrc.close()


        if resolvConfig in open(resolv).read():
            print(language.resolv_already_configured)
            
        else:
            system("cp /etc/resolv.conf /etc/resolv.conf.backup")

            with open(resolv, mode='w') as file_resolv:
                print(language.configuring_resolv, end='', flush=True)
                file_resolv.write(resolvConfig)
                sleep(SLEEP_TIME)
                print(language.done)
                file_resolv.close()


        print(language.stopping_tor, end='', flush=True)
        system('systemctl stop tor')
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)
        
        print(language.starting_tor, end='', flush=True)
        system('sudo -u {0} tor -f {1} > /dev/null'.format(TOR_USER, Torrc))
        sleep(SLEEP_TIME)
        print(language.done)
        
        print(language.iptables_info)
        print(language.setting_iptables, end='', flush=True)
        system(iptables_rules)
        sleep(SLEEP_TIME)
        print(language.done)
        
        print(language.dns_tip)
        
        check_tor('failed')
        
        print(language.circuit_tip)

    except KeyboardInterrupt:
        print()
        exit()


def stop_connecting():
    try:
        print(language.disconnecting_tor)

        system('mv /etc/resolv.conf.backup /etc/resolv.conf')
        sleep(SLEEP_TIME)
        
        print(language.flushing_iptables, end='', flush=True)
        system(IpFlush)
        system('fuser -k 9051/tcp > /dev/null 2>&1')
        sleep(SLEEP_TIME)
        print(language.done)
        
        print(language.restarting_network, end='', flush=True)
        system('systemctl restart --now NetworkManager')
        sleep(7)
        print(language.done)

        print(language.dns_tip)

        check_tor('stopped')

    except KeyboardInterrupt:
        print()
        exit()


def changemac(interface):
    try:
        print(language.changing_mac, end='', flush=True)
        sleep(SLEEP_TIME)
        
        i = getoutput('ifconfig {} down'.format(interface))

        if "ERROR" in i:
            print(language.interface_error.format(interface))
        else:
            print(language.done)
            system('macchanger -r {}'.format(interface))
            system('ifconfig {} up'.format(interface))
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
        print(language.video_tutorials)
        
    except KeyboardInterrupt:
        print()
        exit()

if __name__ == "__main__":
    language = check_lang()
    
    check_windows_check_root()
    
    args = the_argparse(language)

    banner()
    print()
    
    if args.nodelay == True:
        SLEEP_TIME = 0

    if args.list == True:
        print(language.language_list)

    if args.language == True:
        language = choose_lang(language)
        
    if args.update == True:
        check_update()

    if args.dns == True:
        fix_dns()
        
    if args.checkip == True:
        check_tor('stopped')
        
    your_interface = args.mac
    if your_interface != None:
        changemac(your_interface)

    the_id = args.id

    if args.start == True:
        start_connecting()
        print(language.video_tutorials)
        exit()

    if args.stop == True:
        stop_connecting()
        print(language.video_tutorials)
        exit()

    if the_id:
        start_connecting(the_id)
        print(language.video_tutorials)
        exit()

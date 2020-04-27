#!/usr/bin/python3

from torngconf.theme import *
from time import sleep
from os import geteuid, system, path, name
from subprocess import getoutput


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


def check_lang():
    try:
        if path.isfile('torngconf/langconf.txt') == True:
            with open('torngconf/langconf.txt') as file_lang:
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
        with open('torngconf/langconf.txt', mode="w") as file_lang:            
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


def uninstall():
    try:
        choice = str(input(language.wanna_uninstall))
        
        if choice[0].upper() == "Y":
            print(language.uninstalling)
            system('rm -rf /usr/bin/torngconf')
            system('rm /usr/bin/torghostng')
            print(language.uninstalled)
            
        else:
            print(language.torghostng_tip.format('torghostng') + color.END)
            
        print(language.video_tutorials)
        exit()
            
    except KeyboardInterrupt:
        print()
        exit()


language = check_lang()
check_windows_check_root()
banner()


if path.isfile('/usr/bin/torghostng') == True:
    print(language.already_installed.format('TorghostNG'))
    uninstall()

if path.isfile('/usr/bin/pacman') == True:
    INSTALL_PACKAGES = "pacman -S "
        
elif path.isfile('/usr/bin/apt') == True:
    INSTALL_PACKAGES = "apt install "
    
elif path.isfile('/usr/bin/dnf') == True:
    INSTALL_PACKAGES = "dnf install "
        
elif path.isfile('/usr/bin/yum') == True:
    INSTALL_PACKAGES = "yum install "
        
elif path.isfile('/usr/bin/zypper') == True:
    INSTALL_PACKAGES = "zypper install "
        
elif path.isfile('/usr/bin/xbps-install') == True:
    INSTALL_PACKAGES = "xbps-install -S "
        
elif path.isfile('/usr/bin/upgradepkg') == True:
    UPDATE_REPOSITORY = "wget https://slack.conraid.net/repository/slackware64-current"
    INSTALL_PACKAGES = "upgradepkg --install-new "

else:
    print(language.sorry_some_os)
    exit()


def install_package(package):
    try:
        if path.isfile('/usr/bin/'+package) == True:
            print(language.already_installed.format(package))
            
        else:
            print(language.installing.format(package))
            
            if path.isfile('/usr/bin/upgradepkg') == True:
                print(language.downloading.format(package))

                if package == 'tor':
                    system(UPDATE_REPOSITORY + 'tor/tor-0.4.2.7-x86_64-1cf.txz')
                    system(INSTALL_PACKAGES + 'tor-0.4.2.7-x86_64-1cf.txz')
                    
                elif package == 'macchanger':
                    system(UPDATE_REPOSITORY + 'macchanger/macchanger-1.7.0-x86_64-5cf.txz')
                    system(INSTALL_PACKAGES + 'macchanger-1.7.0-x86_64-5cf.txz')
                    
                elif package == 'pip3':
                    system('wget https://packages.slackonly.com/pub/packages/14.1-x86_64/python/python3/python3-3.5.1-x86_64-1_slack.txz')
                    system(INSTALL_PACKAGES + 'python3-3.5.1-x86_64-1_slack.txz')
                
            else:
                if package == 'pip3':
                    package = 'python3-pip'
                    
                    if path.isfile('/usr/bin/pacman') == True:
                        package = 'python-pip'

                system(INSTALL_PACKAGES + package)

            print(icon.success + language.done)
                
            print(language.installed.format(package))
            
            if path.isfile('/usr/bin/upgradepkg') == True:
                print(language.torghostng_tip.format('python3 torghostng.py'))
                print(language.video_tutorials)
                exit()
            
    except KeyboardInterrupt:
        print()
        exit()


def pyinstaller():
    try:
        system('pip2 uninstall pyinstaller')

        if path.isfile('/usr/bin/pyinstaller') == True:
            print(language.already_installed.format('PyInstaller'))
            
        else:
            print(language.installing.format('PyInstaller'))
            system('pip3 install pyinstaller')
            
            print(icon.success + language.done)
            print(language.installed.format('PyInstaller'))
            
        print(language.installing.format('TorghostNG'))
        system('pyinstaller --onefile torghostng.py')
        system('cp -r dist/torghostng /usr/bin && cp -r torngconf /usr/bin')
        system('chmod +x /usr/bin/torghostng')
        
        print(icon.success + language.done)
        print(language.torghostng_tip.format('torghostng') + color.END)
        
    except KeyboardInterrupt:
        print()
        exit()


packages = ['tor','macchanger','pip3']
for package in packages:
    install_package(package)

pyinstaller()
print(language.video_tutorials)
exit()

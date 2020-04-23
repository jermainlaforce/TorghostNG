#!/usr/bin/python3

from torngconf.theme import *
from torghostng import geteuid, system, path, name, getoutput, sleep, argv, check_lang, choose_lang, try_again


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
                lang = eval(file_lang.readline())

                file_lang.close()

                print(lang.applying_language, end='', flush=True)
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
        with open('torngconf/langconf.txt', mode="w") as file_lang:
            file_lang.truncate(0)
            
            print(language.language_list)
            choice = int(input(language.choose_your_lang))
            
            if choice == 1:
                print(English.applying_language, end='', flush=True)
                file_lang.write("English")
                
                print(English.done)
                print(English.current_language + "English")
                return English
            
            if choice == 2:
                print(Vietnamese.applying_language, end='', flush=True)
                file_lang.write("Vietnamese")
                
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

def uninstall():
    try:
        choice = str(input(language.wanna_uninstall))
        
        if choice[0].upper() == "Y":
            print(language.uninstalling)
            system('sudo rm -rf /usr/bin/torngconf')
            system('sudo rm /usr/bin/torghostng')
            print(language.uninstalled)
            exit()
            
        else:
            print(language.torghostng_tip.format('sudo torghostng') + color.END)
            exit()
            
        print(language.video_tutorials)
            
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
    INSTALL_PACKAGES = "sudo pacman -S "
        
elif path.isfile('/usr/bin/apt') == True:
    INSTALL_PACKAGES = "sudo apt install "
    
elif path.isfile('/usr/bin/eopkg') == True:
    INSTALL_PACKAGES = "sudo eopkg install "
        
elif path.isfile('/usr/bin/dnf') == True:
    INSTALL_PACKAGES = "sudo dnf install "
        
elif path.isfile('/usr/bin/yum') == True:
    INSTALL_PACKAGES = "sudo yum install "
        
elif path.isfile('/usr/bin/zypper') == True:
    INSTALL_PACKAGES = "sudo zypper install "
        
elif path.isfile('/usr/bin/apk') == True:
    INSTALL_PACKAGES = "sudo apk add --upgrade "
        
elif path.isfile('/usr/bin/opkg') == True:
    INSTALL_PACKAGES = "sudo opkg install "
        
elif path.isfile('/usr/bin/xbps-install') == True:
    INSTALL_PACKAGES = "sudo xbps-install -S "
        
elif path.isfile('/usr/bin/upgradepkg') == True:
    UPDATE_REPOSITORY = "wget https://slack.conraid.net/repository/slackware64-current/{}"
    INSTALL_PACKAGES = "sudo upgradepkg --install-new "

elif (path.isfile('/usr/bin/pkg') == True) or (path.isfile('/usr/bin/pkg_add') == True):
    print(language.sorry_bsd)
    exit()

elif path.isfile('/usr/bin/swupd') == True:
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
                    system(UPDATE_REPOSITORY.format('tor/tor-0.4.2.7-x86_64-1cf.txz'))
                    system(INSTALL_PACKAGES + 'tor-0.4.2.7-x86_64-1cf.txz')
                    
                elif package == 'macchanger':
                    system(UPDATE_REPOSITORY.format('macchanger/macchanger-1.7.0-x86_64-5cf.txz'))
                    system(INSTALL_PACKAGES + 'macchanger-1.7.0-x86_64-5cf.txz')
                    
                elif package == 'pip3':
                    system('wget https://packages.slackonly.com/pub/packages/14.1-x86_64/python/python3/python3-3.5.1-x86_64-1_slack.txz')
                    system(INSTALL_PACKAGES + 'python3-3.5.1-x86_64-1_slack.txz')
                
            else:
                if package == 'pip3':
                    package = 'python3-pip'

                system(INSTALL_PACKAGES + package)

            print(icon.success + language.done)
                
            print(language.installed.format(package))
            
            if path.isfile('/usr/bin/upgradepkg') == True:
                print(language.torghostng_tip.format('sudo python3 torghostng.py'))
                print(language.video_tutorials)
                exit()
            
    except KeyboardInterrupt:
        print()
        exit()


def pyinstaller():
    try:    
        if path.isfile('/usr/bin/pyinstaller') == True:
            print(language.already_installed.format('PyInstaller'))
            
        else:
            print(language.installing.format('PyInstaller'))
            system('sudo pip2 uninstall pyinstaller')
            system('sudo pip3 install pyinstaller')
            
            print(icon.success + language.done)
            print(language.installed.format('PyInstaller'))
            
        print(language.installing.format('TorghostNG'))
        system('pyinstaller --onefile torghostng.py')
        system('sudo cp -r dist/torghostng /usr/bin')
        system('sudo cp -r torngconf /usr/bin')
        system('chmod +x /usr/bin/torghostng')
        
        print(icon.success + language.done)
        print(language.torghostng_tip.format('sudo torghostng') + color.END)
        print(language.video_tutorials)
        
    except KeyboardInterrupt:
        print()
        exit()


packages = ['tor','macchanger','pip3']
for package in packages:
    install_package(package)

pyinstaller()
exit()

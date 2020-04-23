# About TorghostNG
TorghostNG is a tool that make all your internet traffic anonymized through Tor proxy.

Rewritten from [TorGhost](https://github.com/SusmithKrishnan/torghost) with Python 3.

TorghostNG was tested on:
* Kali Linux
* Manjaro
* ...

# Installing TorghostNG
TorghostNG currently supports:
* GNU/Linux distros that based on Arch Linux
* GNU/Linux distros that based on Debian/Ubuntu
* GNU/Linux distros that based on Fedora, CentOS, RHEL, openSUSE
* [Solus OS](https://getsol.us)
* [Alpine Linux](https://alpinelinux.org)
* [OpenWrt Linux](https://openwrt.org)
* [Void Linux](https://voidlinux.org)
* Anh the elder guy: [Slackware](http://slackware.com)
* (Too much package managers for one day :v)

To install TorghostNG, open your Terminal and enter these commands    
    
    git clone https://github.com/githacktools/TorghostNG
    cd TorghostNG
    sudo python3 install.py
    sudo torghostng
    
But with Slackware, you use `sudo python3 torghostng.py` to run TorghostNG :v

# Help
    TorghostNG 1.0 - Make all your internet traffic anonymized through TOR proxy
    Rewritten from TorGhost with Python 3
    usage: torghostng [-h] -s|-x|-id|-m|-c|-l|--list
    
    OPTIONS:
    -h, --help      Show this help message and exit
    -s, --start     Start connecting to TOR
    -x, --stop      Stop connecting to TOR
    -id COUNTRY ID  Connect to TOR exit node of a specific country. Go to CountryCode.org to search country ID
    -mac INTERFACE  Randomly change MAC address. Use 'ifconfig' to show interface devices
    -c, --checkip   Check your current IP address
    --nodelay       Disable delay time
    -l, --language  Change the display language. English is the default
    --list          Show the available languages list
    -u, --update    Check for update
    --dns           Use this to fix DNS when website address can't be resolved

You can combine multiple choices at the same time, such as:
* `torghostng -s -m INTERFACE`: Changing MAC address before connecting
* `torghostng -c -m INTERFACE`: Checking IP address and changing MAC address
* `torghostng -s -x`: Connecting to Tor anh then stop :v
* ...

If you have any questions, you can watch this [tutorial videos](https://bit.ly/34TNglL) 🙂

I hope you will love it 😃

# Notes before you use Tor
Tor can't help you completely anonymous, just almost:
* [Tor’s Biggest Threat – Correlation Attack](https://theonionweb.com/2016/10/25/tors-biggest-threat-correlation-attack)
* [Is Tor Broken? How the NSA Is Working to De-Anonymize You When Browsing the Deep Web](https://null-byte.wonderhowto.com/how-to/is-tor-broken-nsa-is-working-de-anonymize-you-when-browsing-deep-web-0148933)
* [Use Traffic Analysis to Defeat TOR](https://null-byte.wonderhowto.com/how-to/use-traffic-analysis-defeat-tor-0149100)
* ...

It's recommended that you should use [NoScript](https://noscript.net) before before surfing the web with Tor. NoScript shall block JavaScript/Java/Flash scripts on websites to make sure they won't reveal your real identify.

# And please
* **Don't spam or perform DoS attacks with Tor.** It's not effective, you will only make Tor get hated and waste Tor's money.
* **Don't torrent over Tor.** If you want to keep anonymous while torrenting, use a no-logs VPN please.

[Bittorrent over Tor isn't a good idea](https://blog.torproject.org/bittorrent-over-tor-isnt-good-idea)

[Not anonymous: attack reveals BitTorrent users on Tor network](https://arstechnica.com/tech-policy/2011/04/not-anonymous-attack-reveals-bittorrent-users-on-tor-network)

![Don't torrent over Tor, please](https://github.com/GitHackTools/Store-the-pictures/raw/master/Don't%20torrent%20over%20Tor.png)

# Screenshots of Torghost
* Changing MAC address: `torghostng -m INTERFACE`

![Changing MAC address with TorghostNG](https://github.com/GitHackTools/Store-the-pictures/raw/master/TorghostNG%20changing%20MAC%20address.png)

* Checking IP address: `torghostng -c`

![Checking IP address with TorghostNG](https://github.com/GitHackTools/Store-the-pictures/raw/master/TorghostNG%20checking%20IP%20address.png)

* Disconnecting from Tor: `torghostng -x`

![Disconnecting from Tor network with TorghostNG](https://github.com/GitHackTools/Store-the-pictures/raw/master/TorghostNG%20disconnecting%20from%20TOR.png)

* Connecting to Tor exitnode in a specific country: `torghostng -id COUNTRY ID`

![Connecting to TOR exitnode in a specific country](https://github.com/GitHackTools/Store-the-pictures/raw/master/TorghostNG%20connecting%20to%20TOR%20exitnode%20in%20US.png)

* Uninstalling TorghostNG: `python3 install.py`

![Uninstalling TorghostNG](https://github.com/GitHackTools/Store-the-pictures/raw/master/Uninstalling%20TorghostNG.png)

# Contact to the coder
* Twitter: [@SecureGF](https://twitter.com/securegf)
* Github: here 😃
* Website: [Blogspot](https://githacktools.blogspot.com)

# And finally
You can help me by telling me if you find any bugs or issues. Thank you for using my tool 😊

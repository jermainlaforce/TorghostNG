#!/usr/bin/python3

class color:
    BLUE = '\033[94m'
    CYAN = '\033[36m'
    GREEN = '\033[92m'
    RED = '\033[31m'
    YELLOW = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    BGRED = '\033[41m'
    WHITE = '\033[37m'
    
class icon:
    success = color.GREEN+'[*]'+color.END
    process = color.CYAN+'[+]'+color.END
    info = color.YELLOW+'[i]'+color.END
    error = color.RED+'[!]'+color.END
    question = color.BLUE+'[?]'+color.END

class English:
    options = "OPTIONS"
    downloading = icon.process + "Downloading {}..."
    installing = icon.process + " Installing {}..."
    uninstalling = icon.process + " Uninstalling TorghostNG..."
    uninstalled = icon.success + " {} has been uninstalled"
    installed = icon.success + " {} has been installed"
    already_installed = icon.info + " {} is already installed"
    description = """TorghostNG 1.0 - Make all your internet traffic anonymized through TOR proxy
Rewritten from TorGhost with Python 3"""
    root_please = icon.error + " You must be root, use 'sudo TorghostNG'"
    sorry_windows = icon.error + " Sorry, TorghostNG is not designed for Windows 😛 Use TOR Browser pls"
    sorry_some_os = """I'm sorry, you have to install TOR and macchanger from source by yourself :v I'm too lazy
TOR: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Sorry BSD user, I'm still trying to find way that TorghostNG can fully support for BSD"
    current_language = icon.info + " The current display language: "
    language_list = icon.info + " List of languages:\n    1.English   2.Vietnamese"
    choose_your_lang = icon.question + " Choose your language (1/2): "
    wanna_change_lang = icon.question + " Wanna change the display language? (y/n): "
    wanna_uninstall = icon.question + " Wanna uninstall TorghostNG (y/n): "
    invalid_choice = icon.error + " Invalid choice"
    country_id = "COUNTRY ID"
    help_help = "Show this help message and exit"
    start_help = "Start connecting to TOR"
    stop_help = "Stop connecting to TOR"
    id_help = "Connect to TOR exit node of a specific country. Go to CountryCode.org to search country ID"
    update_help = "Check for update"
    no_delay_help = "Disable delay time"
    changemac_help = "Randomly change MAC address. Use 'ifconfig' to show interface devices"
    language_help = "Change the display language. English is the default"
    language_list_help = "Show the available languages list"
    checkip_help = "Check your current IP address"
    done = color.GREEN+ " Done"+color.END
    iptables_info = icon.info + """ Non-TOR traffic will be blocked by iptables
    Some apps may not be able to connect to the Internet"""
    applying_language = icon.process + " Applying display language..."
    checking_update = icon.process + " Checking TorghostNG update..."
    outofdate = icon.error + " Your TorghostNG is out-of-date"
    uptodate = icon.success + " Your TorghostNG is up-to-date"
    wanna_update = icon.question + " Wanna update your TorghostNG (y/n): "
    updating = icon.process + " Updating TorghostNG to {}..."
    connecting_tor = icon.process + " " + start_help +"..."
    disconnecting_tor = icon.process + " Start disconnecting from TOR..."
    torrc_already_configured = icon.info + " TorghostNG Torrc file is already configured"
    configuring_torrc = icon.process + " Configuring TorghostNG Torrc file..."
    resolv_already_configured = icon.info + " resolv.conf DNS file is already configured"
    configuring_resolv = icon.process + " Configuring resolv.conf DNS file..."
    stopping_tor = icon.process + " Stopping TOR service..."
    starting_tor = icon.process + " Starting new TOR service..."
    setting_iptables = icon.process + " Setting up iptables rules..."
    flushing_iptables = icon.process + " Flushing iptables, resetting to default..."
    checking_ip = icon.process + " Checking your current IP..."
    your_ip = icon.info + " Your current IP address: "
    checking_tor = icon.process + " Checking TOR connection..."
    tor_success = icon.success + " Congratulations! You've been connecting to TOR"
    tor_failed = icon.error + " The connecting process to TOR has failed"
    tor_disconnected = icon.success + " You've been disconnecting from TOR"
    try_again = icon.question + " Wanna try again (y/n): "
    restarting_network = icon.process + " Restarting NetworkManager..."
    changing_mac = icon.process + " Changing your current MAC address..."
    mac_changed = icon.success + " You MAC address has been changed"
    ifconfig_tip = icon.info + color.BOLD + " You can use 'ifconfig' to show interface devices" + color.END
    id_tip = icon.info + color.BOLD + " You can go to https://CountryCode.org to search country id" + color.END
    circuit_tip = icon.info + color.BOLD + " You can request a new TOR circuit by reconnecting it" + color.END
    torghostng_tip = icon.success + color.BOLD + " You can run TorghostNG with '{}'"
    interface_error = icon.error + " There is no interface named {}. Changing failed"
    video_tutorials = icon.info + """" If you have any questions, take a look at TorghostNG Tutorial Videos here: """+ color.BOLD +"""https://bit.ly/34TNglL"""+ color.END +"""
    You will love it, i think :D"""
    
class Vietnamese(English):
    options = "CÁC LỰA CHỌN"
    downloading = icon.process + "Đang tải {}..."
    installing = icon.process + " Đang cài đặt {}..."
    uninstalling = icon.process + " Đang gỡ cài đặt TorghostNG..."
    uninstalled = icon.success + " TorghostNG đã được gỡ cài đặt"
    installed = icon.success + " {} đã được cài đặt"
    already_installed = icon.info + " {} đã được cài đặt sẵn"
    description = """TorghostNG 1.0 - Giúp bạn kết nối Internet ẩn danh qua TOR
Được gõ lại từ TorGhost bằng Python 3"""
    root_please = icon.error + " Phải chạy TorghostNG với quyền root nha, thử 'sudo torghostng' xem"
    sorry_windows = icon.error + " Xin lỗi các bạn dùng Windows nhá ☹ Các bạn dùng TOR Brower nha"
    sorry_some_os = """Với hệ điều hành này thì bạn phải cài TOR với macchanger một cách thủ công thôi :v
TOR: https://github.com/torproject/tor
macchanger: https://github.com/alobbs/macchanger"""
    sorry_bsd = "Mình đang tìm các hỗ trợ BSD, xin lỗi bạn :("
    current_language = icon.info + " Ngôn ngữ hiển thị hiện tại: "
    language_list = icon.info + " Danh sách các ngôn ngữ có sẵn:\n    1.English   2.Vietnamese"
    choose_your_lang = icon.question + " Chọn ngôn ngữ của bạn (1/2): "
    wanna_change_lang = icon.question + " Muốn thay đổi ngôn ngữ hiển thị không? (y/n): "
    wanna_uninstall = icon.question + " Bạn muốn gỡ TorghostNG đi không (y/n): "
    invalid_choice = icon.error + " Lựa chọn không hợp lệ lmao :v"
    country_id = "ID QUỐC GIA"
    help_help = "Hiển thị phần trợ giúp và thoát"
    start_help = "Bắt đầu kết nối đến mạng TOR"
    stop_help = "Ngưng kết nối đến mạng TOR"
    id_help = "Thay đổi địa chỉ IP sang một quốc gia cụ thể. Vô CountryCode.org để xem ID"
    update_help = "Kiểm tra cập nhật"
    no_delay_help = "Tắt hiệu ứng thời gian đi"
    changemac_help = "Thay đổi ngẫu nhiên địa chỉ MAC. Dùng lệnh 'ifconfig' để xem các interface"
    language_help = "Thay đổi ngôn ngữ hiển thị. Tiếng Anh là mặc định"
    language_list_help = "Hiển thị danh sách các ngôn ngữ hiện có"
    checkip_help = "Xem địa chỉ IP hiện tại"
    done = color.GREEN+ " Đã xong"+color.END
    iptables_info = icon.info + """ iptables sẽ chặn các kết nối không đi qua TOR
    Ứng dụng nào thích chơi kết nối một mình một kiểu sẽ bị chặn"""
    applying_language = icon.process + " Đang áp dụng ngôn ngữ hiển thị..."
    checking_update = icon.process + " Đang kiểm tra cập nhật..."
    outofdate = icon.error + " Torghost bạn xài đã cổ lỗ sĩ rồi :v"
    uptodate = icon.success + " TorghostNG bạn xài là bản mới nhất :D"
    wanna_update = icon.question + " Muốn cập nhật Torghost luôn không (y/n): "
    updating = icon.process + " Đang cập nhật TorghostNG lên phiên bản {}..."
    connecting_tor = icon.process + " " + start_help +"..."
    disconnecting_tor = icon.process + " Bắt đầu ngưng kết nối..."
    torrc_already_configured = icon.info + " Tệp cấu hình TOR TorghostNG đã được thiết lập sẵn"
    configuring_torrc = icon.process + " Đang thiết lập tệp cấu hình TOR TorghostNG..."
    resolv_already_configured = icon.info + " Tệp cấu hình DNS resolv.conf đã được thiết lập sẵn"
    configuring_resolv = icon.process + " Đang thiết lập cấu hình DNS resolv.conf..."
    stopping_tor = icon.process + " Đang ngưng tiến trình của TOR..."
    starting_tor = icon.process + " Bắt đầu tiến trình TOR mới..."
    setting_iptables = icon.process + " Đang thiết lập quy tắc cho iptables..."
    flushing_iptables = icon.process + " Đang thiết lập lại iptables về như cũ..."
    checking_ip = icon.process + " Đang kiểm tra địa chỉ IP hiện tại..."
    your_ip = icon.info + " Địa chỉ IP hiện tại: "
    checking_tor = icon.process + " Đang kiểm tra kết nối đến mạng TOR..."
    tor_success = icon.success + " Đã kết nối đến mạng TOR"
    tor_failed = icon.error + " Quá trình kết nối đến mạng TOR thất bại"
    tor_disconnected = icon.success + " Đã ngưng kết nối khỏi mạng TOR"
    try_again = icon.question + " Bạn có muốn thử lại không (y/n): "
    restarting_network = icon.process + " Đang khởi động lại NetworkManager..."
    changing_mac = icon.process + " Đang thay đổi địa chỉ MAC hiện tại..."
    mac_changed = icon.success + " Đã thay đổi địa chỉ MAC"
    ifconfig_tip = icon.info + color.BOLD + " Bạn có thể dùng lệnh 'ifconfig' để xem các interface trong máy" + color.END
    id_tip = icon.info + color.BOLD + " Bạn có thể vô https://CountryCode.org để tìm ID của từng quốc gia" + color.END
    circuit_tip = icon.info + color.BOLD + " Bạn có thể chuyển một mạch TOR mới bằng cách kết nối lại" + color.END
    torghostng_tip = icon.success + color.BOLD + " Bạn có thể chạy TorghostNG với lệnh '{}'"
    interface_error = icon.error + " Không có interface nào tên {}. Thay đổi thất bại"
    video_tutorials = icon.info + " Nếu có thắc mắc gì thì các cậu xem video hướng dẫn nha: "+ color.BOLD +"https://bit.ly/34TNglL"+ color.END
    
the_banner = color.GREEN + """ _____               _               _   _   _  ____ 
|_   _|__  _ __ __ _| |__   ___  ___| |_| \ | |/ ___|
  | |/ _ \| '__/ _` | '_ \ / _ \/ __| __|  \| | |  _ 
  | | (_) | | | (_| | | | | (_) \__ \ |_| |\  | |_| |
  |_|\___/|_|  \__, |_| |_|\___/|___/\__|_| \_|\____|
               |___/""" + color.END

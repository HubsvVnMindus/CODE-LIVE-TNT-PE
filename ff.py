import random
import time
from datetime import datetime
import re
from colorama import init, Fore
import sys
import os
import json
import select

# Khởi tạo colorama
init()

# Biến toàn cục
user_id = ""
user_data = {}  # Lưu dữ liệu người dùng
DATA_FILE = "user_data.json"
current_lang = "vi"  # Ngôn ngữ mặc định
language_data = {}

# ==========================
# NGÔN NGỮ GIAO DIỆN
# ==========================
def load_language(lang="vi"):
    languages = {
        "vi": {
            "welcome": "HUNG-TOOL HACK FREE FIRE 2025",
            "invalid_choice": "Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 7.",
            "exit_message": "Đang thoát tool... Cảm ơn bạn đã sử dụng!",
            "history_title": "LỊCH SỬ GIAO DỊCH - ID: {}",
            "no_history": "Chưa có giao dịch nào!",
            "no_data": "Chưa có dữ liệu để hiển thị biểu đồ!",
            "chart_displayed": "Biểu đồ thống kê đã được hiển thị!",
            "password_prompt": "Nhập mật khẩu (còn {} lần): ",
            "password_success": "Đăng nhập thành công!",
            "password_fail": "Mật khẩu sai!",
            "password_limit": "Hết lượt thử. Thoát chương trình.",
            "no_id": "Chưa có ID nào được lưu. Vui lòng nhập ID mới.",
            "id_prompt": "Nhập ID mới (chỉ số, ví dụ: 123456789): ",
            "id_invalid": "ID không hợp lệ! Chỉ được chứa số.",
            "id_exists": "ID đã tồn tại! Vui lòng nhập ID khác.",
            "id_added": "ID {} đã được thêm!",
            "id_selected": "Đã chọn ID: {}",
            "invalid_selection": "Lựa chọn không hợp lệ!",
            "server_connecting": "Đang kết nối đến server...",
            "server_success": "Kết nối thành công!",
            "server_fail": "Kết nối thất bại! Vui lòng thử lại sau.",
            "hack_limit": "Bạn đã đạt giới hạn hack trong ngày!",
            "diamonds_received": "Nhận được {} kim cương! Tổng: {}",
            "coins_received": "Nhận được {} vàng! Tổng: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "select_language": "Chọn ngôn ngữ / Select language:",
            "lang_vi": "1. Tiếng Việt",
            "lang_en": "2. English",
            "lang_prompt": "Nhập lựa chọn (1-2): "
        },
        "en": {
            "welcome": "HUNG-TOOL FREE FIRE HACK 2025",
            "invalid_choice": "Invalid choice! Please select from 1 to 7.",
            "exit_message": "Exiting tool... Thank you for using!",
            "history_title": "TRANSACTION HISTORY - ID: {}",
            "no_history": "No transactions yet!",
            "no_data": "No data to display chart!",
            "chart_displayed": "Statistics chart has been displayed!",
            "password_prompt": "Enter password ({} attempts left): ",
            "password_success": "Login successful!",
            "password_fail": "Incorrect password!",
            "password_limit": "No attempts left. Exiting program.",
            "no_id": "No IDs stored yet. Please enter a new ID.",
            "id_prompt": "Enter new ID (numbers only, e.g., 123456789): ",
            "id_invalid": "Invalid ID! Must contain only numbers.",
            "id_exists": "ID already exists! Please enter a different ID.",
            "id_added": "ID {} has been added!",
            "id_selected": "Selected ID: {}",
            "invalid_selection": "Invalid selection!",
            "server_connecting": "Connecting to server...",
            "server_success": "Connection successful!",
            "server_fail": "Connection failed! Please try again later.",
            "hack_limit": "You have reached the daily hack limit!",
            "diamonds_received": "Received {} diamonds! Total: {}",
            "coins_received": "Received {} coins! Total: {}",
            "press_enter": "Press Enter to continue...",
            "select_language": "Select language:",
            "lang_vi": "1. Vietnamese",
            "lang_en": "2. English",
            "lang_prompt": "Enter choice (1-2): "
        }
    }
    return languages.get(lang, languages["vi"])

# ==========================
# LÀM VIỆC VỚI DỮ LIỆU
# ==========================
def load_user_data():
    global user_data
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                user_data = json.load(file)
        except json.JSONDecodeError:
            user_data = {}
    else:
        user_data = {}

def save_user_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

# ==========================
# HIỆU ỨNG & ĐĂNG NHẬP
# ==========================
def print_typing(text, delay=0.05, skipable=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
        if skipable and sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            input()
            print(text[len(text)-len(text):], end="")
            break
    print()

def login():
    correct_password = "hungtool2025"
    attempts = 3
    while attempts > 0:
        password = input(f"{Fore.GREEN}{language_data['password_prompt'].format(attempts)}{Fore.RESET}")
        if password == correct_password:
            print(f"{Fore.GREEN}{language_data['password_success']}{Fore.RESET}")
            return True
        attempts -= 1
        print(f"{Fore.RED}{language_data['password_fail']}{Fore.RESET}")
    print(f"{Fore.RED}{language_data['password_limit']}{Fore.RESET}")
    sys.exit()

# ==========================
# QUẢN LÝ ID NGƯỜI DÙNG
# ==========================
def get_new_user_id():
    global user_id
    while True:
        user_id = input(f"{Fore.GREEN}{language_data['id_prompt']}{Fore.RESET}")
        if re.match(r'^\d+$', user_id):
            if user_id not in user_data:
                user_data[user_id] = {'total_diamonds': 0, 'total_coins': 0, 'history': [], 'last_hack_date': '', 'hack_count': 0}
                save_user_data()
                print(f"{Fore.GREEN}{language_data['id_added'].format(user_id)}{Fore.RESET}")
                break
            else:
                print(f"{Fore.RED}{language_data['id_exists']}{Fore.RESET}")
        else:
            print(f"{Fore.RED}{language_data['id_invalid']}{Fore.RESET}")

def select_user_id():
    global user_id
    load_user_data()
    if not user_data:
        print(f"{Fore.RED}[HUNG-TOOL]{Fore.RESET} {language_data['no_id']}")
        get_new_user_id()
        return
    print(f"\n{Fore.CYAN}Danh sách ID đã lưu:{Fore.RESET}")
    for idx, uid in enumerate(user_data.keys(), 1):
        print(f"{Fore.YELLOW}{idx}. {uid} (Kim cương: {user_data[uid]['total_diamonds']}, Vàng: {user_data[uid]['total_coins']}){Fore.RESET}")
    print(f"{Fore.CYAN}0. Thêm ID mới{Fore.RESET}")
    choice = input(f"\n{Fore.GREEN}Chọn số thứ tự ID hoặc 0 để thêm mới: {Fore.RESET}")
    if choice == '0':
        get_new_user_id()
    else:
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(user_data):
                user_id = list(user_data.keys())[choice]
                print(f"{Fore.GREEN}{language_data['id_selected'].format(user_id)}{Fore.RESET}")
            else:
                print(f"{Fore.RED}{language_data['invalid_selection']}{Fore.RESET}")
                time.sleep(1)
                select_user_id()
        except ValueError:
            print(f"{Fore.RED}{language_data['invalid_selection']}{Fore.RESET}")
            time.sleep(1)
            select_user_id()

# ==========================
# CHỨC NĂNG TOOL
# ==========================
def simulate_server_connection():
    print(f"{Fore.YELLOW}{language_data['server_connecting']}{Fore.RESET}")
    for _ in range(3):
        print(f"{Fore.YELLOW}.{Fore.RESET}", end="", flush=True)
        time.sleep(0.5)
    success = random.choice([True, False])
    if success:
        print(f"{Fore.GREEN}{language_data['server_success']}{Fore.RESET}")
        return True
    else:
        print(f"{Fore.RED}{language_data['server_fail']}{Fore.RESET}")
        return False

def can_hack_today():
    today = datetime.now().strftime('%Y-%m-%d')
    if 'last_hack_date' not in user_data[user_id]:
        user_data[user_id]['last_hack_date'] = today
        user_data[user_id]['hack_count'] = 0
    elif user_data[user_id]['last_hack_date'] != today:
        user_data[user_id]['last_hack_date'] = today
        user_data[user_id]['hack_count'] = 0
    if user_data[user_id]['hack_count'] >= 3:
        print(f"{Fore.RED}{language_data['hack_limit']}{Fore.RESET}")
        return False
    return True

def hack_diamonds():
    if not can_hack_today():
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    if simulate_server_connection():
        diamonds = random.randint(100, 1000)
        user_data[user_id]['total_diamonds'] += diamonds
        user_data[user_id]['history'].append({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Kim cương' if current_lang == "vi" else "Diamonds",
            'amount': diamonds
        })
        user_data[user_id]['hack_count'] += 1
        save_user_data()
        print(f"{Fore.GREEN}{language_data['diamonds_received'].format(diamonds, user_data[user_id]['total_diamonds'])}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def hack_coins():
    if not can_hack_today():
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    if simulate_server_connection():
        coins = random.randint(500, 5000)
        user_data[user_id]['total_coins'] += coins
        user_data[user_id]['history'].append({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Vàng' if current_lang == "vi" else "Coins",
            'amount': coins
        })
        user_data[user_id]['hack_count'] += 1
        save_user_data()
        print(f"{Fore.GREEN}{language_data['coins_received'].format(coins, user_data[user_id]['total_coins'])}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def view_history():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          {language_data['history_title'].format(user_id)}          ║{Fore.RESET}", delay=0.02)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    if not user_data[user_id]['history']:
        print(f"{Fore.RED}{language_data['no_history']}{Fore.RESET}")
    else:
        for entry in user_data[user_id]['history']:
            print(f"{Fore.CYAN}{entry['time']}: {entry['type']} +{entry['amount']}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def show_stats_chart():
    if not user_data:
        print(f"{Fore.RED}{language_data['no_data']}{Fore.RESET}")
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    print(f"{Fore.GREEN}{language_data['chart_displayed']}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

# ==========================
# MENU CHÍNH
# ==========================
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          {language_data['welcome']}            ║{Fore.RESET}", delay=0.02)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    print(f"{Fore.CYAN}ID: {user_id} | Kim cương: {user_data[user_id].get('total_diamonds', 0)} | Vàng: {user_data[user_id].get('total_coins', 0)}{Fore.RESET}")
    print(f"{Fore.GREEN}┌──────────────────────────────────────────────────────┐{Fore.RESET}")
    options = [
        "1. Hack kim cương" if current_lang == "vi" else "1. Hack diamonds",
        "2. Hack vàng" if current_lang == "vi" else "2. Hack coins",
        "3. Xem lịch sử giao dịch" if current_lang == "vi" else "3. View transaction history",
        "4. Xem thống kê" if current_lang == "vi" else "4. View statistics",
        "5. Đổi ID" if current_lang == "vi" else "5. Change ID",
        "6. Chọn ngôn ngữ" if current_lang == "vi" else "6. Select language",
        "7. Thoát tool" if current_lang == "vi" else "7. Exit tool",
    ]
    for option in options:
        num, text = option.split(". ", 1)
        print(f"{Fore.GREEN}│{Fore.RESET} {Fore.YELLOW}{num}.{Fore.RESET} {Fore.CYAN}{text:<50}{Fore.RESET}{Fore.GREEN}│{Fore.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"{Fore.GREEN}└──────────────────────────────────────────────────────┘{Fore.RESET}")

# ==========================
# MAIN CHƯƠNG TRÌNH
# ==========================
def main():
    global language_data, current_lang
    language_data = load_language(current_lang)
    if login():
import random
import time
from datetime import datetime
import re
from colorama import init, Fore
import sys
import os
import json
import select

# Khởi tạo colorama
init()

# Biến toàn cục
user_id = ""
user_data = {}  # Lưu dữ liệu người dùng
DATA_FILE = "user_data.json"
current_lang = "vi"  # Ngôn ngữ mặc định
language_data = {}

# ==========================
# NGÔN NGỮ GIAO DIỆN
# ==========================
def load_language(lang="vi"):
    languages = {
        "vi": {
            "welcome": "HUNG-TOOL HACK FREE FIRE 2025",
            "invalid_choice": "Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 7.",
            "exit_message": "Đang thoát tool... Cảm ơn bạn đã sử dụng!",
            "history_title": "LỊCH SỬ GIAO DỊCH - ID: {}",
            "no_history": "Chưa có giao dịch nào!",
            "no_data": "Chưa có dữ liệu để hiển thị biểu đồ!",
            "chart_displayed": "Biểu đồ thống kê đã được hiển thị!",
            "password_prompt": "Nhập mật khẩu (còn {} lần): ",
            "password_success": "Đăng nhập thành công!",
            "password_fail": "Mật khẩu sai!",
            "password_limit": "Hết lượt thử. Thoát chương trình.",
            "no_id": "Chưa có ID nào được lưu. Vui lòng nhập ID mới.",
            "id_prompt": "Nhập ID mới (chỉ số, ví dụ: 123456789): ",
            "id_invalid": "ID không hợp lệ! Chỉ được chứa số.",
            "id_exists": "ID đã tồn tại! Vui lòng nhập ID khác.",
            "id_added": "ID {} đã được thêm!",
            "id_selected": "Đã chọn ID: {}",
            "invalid_selection": "Lựa chọn không hợp lệ!",
            "server_connecting": "Đang kết nối đến server...",
            "server_success": "Kết nối thành công!",
            "server_fail": "Kết nối thất bại! Vui lòng thử lại sau.",
            "hack_limit": "Bạn đã đạt giới hạn hack trong ngày!",
            "diamonds_received": "Nhận được {} kim cương! Tổng: {}",
            "coins_received": "Nhận được {} vàng! Tổng: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "select_language": "Chọn ngôn ngữ / Select language:",
            "lang_vi": "1. Tiếng Việt",
            "lang_en": "2. English",
            "lang_prompt": "Nhập lựa chọn (1-2): "
        },
        "en": {
            "welcome": "HUNG-TOOL FREE FIRE HACK 2025",
            "invalid_choice": "Invalid choice! Please select from 1 to 7.",
            "exit_message": "Exiting tool... Thank you for using!",
            "history_title": "TRANSACTION HISTORY - ID: {}",
            "no_history": "No transactions yet!",
            "no_data": "No data to display chart!",
            "chart_displayed": "Statistics chart has been displayed!",
            "password_prompt": "Enter password ({} attempts left): ",
            "password_success": "Login successful!",
            "password_fail": "Incorrect password!",
            "password_limit": "No attempts left. Exiting program.",
            "no_id": "No IDs stored yet. Please enter a new ID.",
            "id_prompt": "Enter new ID (numbers only, e.g., 123456789): ",
            "id_invalid": "Invalid ID! Must contain only numbers.",
            "id_exists": "ID already exists! Please enter a different ID.",
            "id_added": "ID {} has been added!",
            "id_selected": "Selected ID: {}",
            "invalid_selection": "Invalid selection!",
            "server_connecting": "Connecting to server...",
            "server_success": "Connection successful!",
            "server_fail": "Connection failed! Please try again later.",
            "hack_limit": "You have reached the daily hack limit!",
            "diamonds_received": "Received {} diamonds! Total: {}",
            "coins_received": "Received {} coins! Total: {}",
            "press_enter": "Press Enter to continue...",
            "select_language": "Select language:",
            "lang_vi": "1. Vietnamese",
            "lang_en": "2. English",
            "lang_prompt": "Enter choice (1-2): "
        }
    }
    return languages.get(lang, languages["vi"])

# ==========================
# LÀM VIỆC VỚI DỮ LIỆU
# ==========================
def load_user_data():
    global user_data
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as file:
                user_data = json.load(file)
        except json.JSONDecodeError:
            user_data = {}
    else:
        user_data = {}

def save_user_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

# ==========================
# HIỆU ỨNG & ĐĂNG NHẬP
# ==========================
def print_typing(text, delay=0.05, skipable=True):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
        if skipable and sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            input()
            print(text[len(text)-len(text):], end="")
            break
    print()

def login():
    correct_password = "hungtool2025"
    attempts = 3
    while attempts > 0:
        password = input(f"{Fore.GREEN}{language_data['password_prompt'].format(attempts)}{Fore.RESET}")
        if password == correct_password:
            print(f"{Fore.GREEN}{language_data['password_success']}{Fore.RESET}")
            return True
        attempts -= 1
        print(f"{Fore.RED}{language_data['password_fail']}{Fore.RESET}")
    print(f"{Fore.RED}{language_data['password_limit']}{Fore.RESET}")
    sys.exit()

# ==========================
# QUẢN LÝ ID NGƯỜI DÙNG
# ==========================
def get_new_user_id():
    global user_id
    while True:
        user_id = input(f"{Fore.GREEN}{language_data['id_prompt']}{Fore.RESET}")
        if re.match(r'^\d+$', user_id):
            if user_id not in user_data:
                user_data[user_id] = {'total_diamonds': 0, 'total_coins': 0, 'history': [], 'last_hack_date': '', 'hack_count': 0}
                save_user_data()
                print(f"{Fore.GREEN}{language_data['id_added'].format(user_id)}{Fore.RESET}")
                break
            else:
                print(f"{Fore.RED}{language_data['id_exists']}{Fore.RESET}")
        else:
            print(f"{Fore.RED}{language_data['id_invalid']}{Fore.RESET}")

def select_user_id():
    global user_id
    load_user_data()
    if not user_data:
        print(f"{Fore.RED}[HUNG-TOOL]{Fore.RESET} {language_data['no_id']}")
        get_new_user_id()
        return
    print(f"\n{Fore.CYAN}Danh sách ID đã lưu:{Fore.RESET}")
    for idx, uid in enumerate(user_data.keys(), 1):
        print(f"{Fore.YELLOW}{idx}. {uid} (Kim cương: {user_data[uid]['total_diamonds']}, Vàng: {user_data[uid]['total_coins']}){Fore.RESET}")
    print(f"{Fore.CYAN}0. Thêm ID mới{Fore.RESET}")
    choice = input(f"\n{Fore.GREEN}Chọn số thứ tự ID hoặc 0 để thêm mới: {Fore.RESET}")
    if choice == '0':
        get_new_user_id()
    else:
        try:
            choice = int(choice) - 1
            if 0 <= choice < len(user_data):
                user_id = list(user_data.keys())[choice]
                print(f"{Fore.GREEN}{language_data['id_selected'].format(user_id)}{Fore.RESET}")
            else:
                print(f"{Fore.RED}{language_data['invalid_selection']}{Fore.RESET}")
                time.sleep(1)
                select_user_id()
        except ValueError:
            print(f"{Fore.RED}{language_data['invalid_selection']}{Fore.RESET}")
            time.sleep(1)
            select_user_id()

# ==========================
# CHỨC NĂNG TOOL
# ==========================
def simulate_server_connection():
    print(f"{Fore.YELLOW}{language_data['server_connecting']}{Fore.RESET}")
    for _ in range(3):
        print(f"{Fore.YELLOW}.{Fore.RESET}", end="", flush=True)
        time.sleep(0.5)
    success = random.choice([True, False])
    if success:
        print(f"{Fore.GREEN}{language_data['server_success']}{Fore.RESET}")
        return True
    else:
        print(f"{Fore.RED}{language_data['server_fail']}{Fore.RESET}")
        return False

def can_hack_today():
    today = datetime.now().strftime('%Y-%m-%d')
    if 'last_hack_date' not in user_data[user_id]:
        user_data[user_id]['last_hack_date'] = today
        user_data[user_id]['hack_count'] = 0
    elif user_data[user_id]['last_hack_date'] != today:
        user_data[user_id]['last_hack_date'] = today
        user_data[user_id]['hack_count'] = 0
    if user_data[user_id]['hack_count'] >= 3:
        print(f"{Fore.RED}{language_data['hack_limit']}{Fore.RESET}")
        return False
    return True

def hack_diamonds():
    if not can_hack_today():
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    if simulate_server_connection():
        diamonds = random.randint(100, 1000)
        user_data[user_id]['total_diamonds'] += diamonds
        user_data[user_id]['history'].append({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Kim cương' if current_lang == "vi" else "Diamonds",
            'amount': diamonds
        })
        user_data[user_id]['hack_count'] += 1
        save_user_data()
        print(f"{Fore.GREEN}{language_data['diamonds_received'].format(diamonds, user_data[user_id]['total_diamonds'])}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def hack_coins():
    if not can_hack_today():
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    if simulate_server_connection():
        coins = random.randint(500, 5000)
        user_data[user_id]['total_coins'] += coins
        user_data[user_id]['history'].append({
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'type': 'Vàng' if current_lang == "vi" else "Coins",
            'amount': coins
        })
        user_data[user_id]['hack_count'] += 1
        save_user_data()
        print(f"{Fore.GREEN}{language_data['coins_received'].format(coins, user_data[user_id]['total_coins'])}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def view_history():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          {language_data['history_title'].format(user_id)}          ║{Fore.RESET}", delay=0.02)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    if not user_data[user_id]['history']:
        print(f"{Fore.RED}{language_data['no_history']}{Fore.RESET}")
    else:
        for entry in user_data[user_id]['history']:
            print(f"{Fore.CYAN}{entry['time']}: {entry['type']} +{entry['amount']}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

def show_stats_chart():
    if not user_data:
        print(f"{Fore.RED}{language_data['no_data']}{Fore.RESET}")
        input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")
        return
    print(f"{Fore.GREEN}{language_data['chart_displayed']}{Fore.RESET}")
    input(f"{Fore.YELLOW}{language_data['press_enter']}{Fore.RESET}")

# ==========================
# MENU CHÍNH
# ==========================
def display_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          {language_data['welcome']}            ║{Fore.RESET}", delay=0.02)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    print(f"{Fore.CYAN}ID: {user_id} | Kim cương: {user_data[user_id].get('total_diamonds', 0)} | Vàng: {user_data[user_id].get('total_coins', 0)}{Fore.RESET}")
    print(f"{Fore.GREEN}┌──────────────────────────────────────────────────────┐{Fore.RESET}")
    options = [
        "1. Hack kim cương" if current_lang == "vi" else "1. Hack diamonds",
        "2. Hack vàng" if current_lang == "vi" else "2. Hack coins",
        "3. Xem lịch sử giao dịch" if current_lang == "vi" else "3. View transaction history",
        "4. Xem thống kê" if current_lang == "vi" else "4. View statistics",
        "5. Đổi ID" if current_lang == "vi" else "5. Change ID",
        "6. Chọn ngôn ngữ" if current_lang == "vi" else "6. Select language",
        "7. Thoát tool" if current_lang == "vi" else "7. Exit tool",
    ]
    for option in options:
        num, text = option.split(". ", 1)
        print(f"{Fore.GREEN}│{Fore.RESET} {Fore.YELLOW}{num}.{Fore.RESET} {Fore.CYAN}{text:<50}{Fore.RESET}{Fore.GREEN}│{Fore.RESET}")
        sys.stdout.flush()
        time.sleep(0.1)
    print(f"{Fore.GREEN}└──────────────────────────────────────────────────────┘{Fore.RESET}")

# ==========================
# MAIN CHƯƠNG TRÌNH
# ==========================
def main():
    global language_data, current_lang
    language_data = load_language(current_lang)
    if login():
        select_user_id()
        while True:
            display_menu()
            print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] {language_data['lang_prompt'].replace('1-2','1-7')}{Fore.RESET}", end="")
            choice = input()
            if choice == "1":
                hack_diamonds()
            elif choice == "2":
                hack_coins()
            elif choice == "3":
                view_history()
            elif choice == "4":
                show_stats_chart()
            elif choice == "5":
                select_user_id()
            elif choice == "6":
                print(f"\n{Fore.CYAN}{language_data['select_language']}{Fore.RESET}")
                print(f"{Fore.CYAN}{language_data['lang_vi']}{Fore.RESET}")
                print(f"{Fore.CYAN}{language_data['lang_en']}{Fore.RESET}")
                lang_choice = input(f"{Fore.GREEN}{language_data['lang_prompt']}{Fore.RESET}")
                current_lang = "vi" if lang_choice == "1" else "en"
                language_data = load_language(current_lang)
            elif choice == "7":
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET} {language_data['exit_message']}")
                time.sleep(1)
                break
            else:
                print(f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET} {language_data['invalid_choice']}")
                time.sleep(1)

if __name__ == "__main__":
    main()


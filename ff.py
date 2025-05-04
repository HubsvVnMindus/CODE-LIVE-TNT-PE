import random
import time
from datetime import datetime
import re
from colorama import init, Fore
import sys
import os
import json

# Khởi tạo colorama
init()

# Biến toàn cục để lưu ID
user_id = ""
user_data = {}  # Lưu trữ dữ liệu người dùng {ID: total_diamonds}

# Đường dẫn file lưu trữ dữ liệu
DATA_FILE = "user_data.json"

def load_user_data():
    """Load dữ liệu người dùng từ file JSON"""
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
    """Lưu dữ liệu người dùng vào file JSON"""
    with open(DATA_FILE, 'w') as file:
        json.dump(user_data, file, indent=4)

def print_typing(text, delay=0.05):
    """Hiệu ứng gõ chữ cho văn bản"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def select_user_id():
    """Hiển thị menu chọn ID hoặc thêm ID mới"""
    global user_id
    load_user_data()
    if not user_data:
        print(
            f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
            f"{Fore.WHITE}-->>{Fore.RESET}"
            f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
            f"Chưa có ID nào được lưu. Vui lòng nhập ID mới."
        )
        get_new_user_id()
        return

    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          HUNG-TOOL HACK FREE FIRE 2025            {Fore.RESET}", delay=0.03)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    print(f"{Fore.GREEN}┌─────────────────── Danh sách ID ───────────────────┐{Fore.RESET}")
    
    # Hiển thị danh sách ID đã lưu
    id_list = list(user_data.keys())
    for idx, uid in enumerate(id_list, 1):
        print(
            f"{Fore.GREEN}│{Fore.RESET} {Fore.YELLOW}{idx}.{Fore.RESET} "
            f"ID: {Fore.CYAN}{uid}{Fore.RESET} | Tổng kim cương: {Fore.YELLOW}{user_data[uid]['total_diamonds']} 💎{Fore.RESET}"
        )
    print(
        f"{Fore.GREEN}│{Fore.RESET} {Fore.YELLOW}{len(id_list) + 1}.{Fore.RESET} "
        f"{Fore.CYAN}Thêm ID mới{Fore.RESET}"
    )
    print(f"{Fore.GREEN}└────────────────────────────────────────────────────┘{Fore.RESET}")

    while True:
        print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] Chọn ID (1-{len(id_list) + 1}): {Fore.RESET}", end="")
        choice = input()
        if choice.isdigit() and 1 <= int(choice) <= len(id_list) + 1:
            if int(choice) == len(id_list) + 1:
                get_new_user_id()
            else:
                user_id = id_list[int(choice) - 1]
                print(
                    f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                    f"{Fore.WHITE}-->>{Fore.RESET}"
                    f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                    f"Đã chọn ID {Fore.CYAN}{user_id}{Fore.RESET} "
                    f"(Tổng kim cương: {Fore.YELLOW}{user_data[user_id]['total_diamonds']} 💎{Fore.RESET})"
                )
                time.sleep(1)
            break
        else:
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến {len(id_list) + 1}."
            )

def get_new_user_id():
    """Nhập và xác thực ID mới"""
    global user_id
    while True:
        print(f"{Fore.YELLOW}Nhập ID game Free Fire (8-11 Số): {Fore.RESET}", end="")
        user_id = input()
        if re.match(r'^\d{8,11}$', user_id):
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"ID {Fore.CYAN}{user_id}{Fore.RESET} hợp lệ!"
            )
            if user_id not in user_data:
                user_data[user_id] = {"total_diamonds": 0}
                save_user_data()
            time.sleep(1)
            break
        else:
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"ID {Fore.CYAN}{user_id}{Fore.RESET} không hợp lệ! ID Free Fire phải là 8-11 chữ số."
            )

def hack_diamonds():
    global user_data
    print(
        f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
        f"{Fore.WHITE}-->>{Fore.RESET}"
        f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
        f"Đang kết nối với server hack kim cương Free Fire cho ID {Fore.CYAN}{user_id}{Fore.RESET}..."
    )
    for _ in range(30):
        print("▬", end="", flush=True)
        time.sleep(0.5)
    print()
    print(f"Nhấn Ctrl+C để dừng và quay lại menu.{Fore.RESET}")
    time.sleep(1)
    elapsed_seconds = 0  # Biến đếm giây tăng dần
    try:
        while True:
            # Hiển thị thông báo trước khi bắt đầu mỗi lần hack
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[20s]{Fore.RESET}"
                f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"Đang hack kim cương cho ID {Fore.CYAN}{user_id}{Fore.RESET}..."
            )
            diamonds = random.randint(0, 2)
            user_data[user_id]["total_diamonds"] += diamonds
            save_user_data()
            # Đếm ngược từ 20 về 0, hiển thị trên cùng một dòng
            for countdown in range(20, -1, -1):
                print(
                    f"\r{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                    f"{Fore.WHITE}-->>{Fore.RESET}"
                    f"{Fore.GREEN}[{countdown}]{Fore.RESET}"
                    f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                    f"Đang hack kim cương cho ID {Fore.CYAN}{user_id}{Fore.RESET}...",
                    end=""
                )
                sys.stdout.flush()
                time.sleep(1)
                elapsed_seconds += 1
            # Sau 20 giây, in kết quả xuống dòng mới
            print(
                f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.YELLOW}[Đã chạy: {elapsed_seconds}s]{Fore.RESET}"
                f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"ID {Fore.CYAN}{user_id}{Fore.RESET} nhận được {Fore.WHITE}{diamonds} 💎 kim cương {Fore.RESET}"
                f" | Tổng nhận: {Fore.YELLOW}{user_data[user_id]['total_diamonds']} 💎{Fore.RESET}"
            )
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
            f"{Fore.WHITE}-->>{Fore.RESET}"
            f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
            f"Đã dừng hack kim cương. Tổng kim cương nhận được: {Fore.YELLOW}{user_data[user_id]['total_diamonds']} 💎{Fore.RESET}"
            f" | Thời gian đã chạy: {Fore.YELLOW}{elapsed_seconds}s{Fore.RESET}"
        )
        save_user_data()
        time.sleep(1)

def hack_coins():
    print(
        f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
        f"{Fore.WHITE}-->>{Fore.RESET}"
        f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
        f"Đang kết nối với server hack Vàng Free Fire..."
    )
    for _ in range(30):
        print("▬", end="", flush=True)
        time.sleep(0.5)
    print()
    print(
        f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
        f"{Fore.WHITE}-->>{Fore.RESET}"
        f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
        f"Kết nối server thất bại. Vui lòng thử lại sau!"
    )
    time.sleep(5)

def get_game_name():
    print(
        f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
        f"{Fore.WHITE}-->>{Fore.RESET}"
        f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
        f"Nhập ID game Free Fire (8-11 chữ số): {Fore.RESET}",
        end=""
    )
    temp_id = input()
    time.sleep(1)
    if re.match(r'^\d{8,11}$', temp_id):
        print(
            f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
            f"{Fore.WHITE}-->>{Fore.RESET}"
            f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
            f"ID {Fore.CYAN}{temp_id}{Fore.RESET} hợp lệ!"
        )
    else:
        print(
            f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
            f"{Fore.WHITE}-->>{Fore.RESET}"
            f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
            f"ID {Fore.CYAN}{temp_id}{Fore.RESET} không hợp lệ! ID Free Fire phải là 8-11 chữ số."
        )
    time.sleep(1)
    print(
        f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
        f"{Fore.WHITE}-->>{Fore.RESET}"
        f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
        f"Lưu ý: Đây chỉ là mô phỏng, không kết nối với Free Fire thật!"
    )

def display_menu():
    """Hiển thị menu với hiệu ứng xuất hiện dần, xóa màn hình trước"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          HUNG-TOOL HACK FREE FIRE 2025            {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║ {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║Lưu ý: Đây là bản kết nối với server của mình.      {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║và đây cũng là bản test server nên kim cương  {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║hay là vàng sẽ về acc sau 24h {Fore.RESET}", delay=0.03)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    # Đảm bảo user_id tồn tại và lấy total_diamonds trực tiếp
    total_diamonds = user_data[user_id]['total_diamonds'] if user_id in user_data else 0
    print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] Người chơi: ID: {Fore.CYAN}{user_id} | Tổng nhận: {Fore.YELLOW}{total_diamonds} 💎{Fore.RESET} {Fore.GREEN}Phiên bản: V1.2{Fore.RESET}")
    print(f"{Fore.GREEN}┌──────────────────────────────────────────────────────┐{Fore.RESET}")
    
    options = [
        f"1. Hack kim cương        {Fore.GREEN}[SERVER ON]{Fore.RESET}",
        f"2. Hack vàng             {Fore.RED}[SERVER OFF]{Fore.RESET}",
        "3. Thoát tool",
    ]
    for option in options:
        num, text = option.split(". ", 1)
        print(f"{Fore.GREEN}│{Fore.RESET} {Fore.YELLOW}{num}.{Fore.RESET} {Fore.CYAN}{text:<50}{Fore.RESET}{Fore.GREEN}│{Fore.RESET}")
        sys.stdout.flush()
        time.sleep(0.2)

    print(f"{Fore.GREEN}└──────────────────────────────────────────────────────┘{Fore.RESET}")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print_typing(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}", delay=0.02)
    print_typing(f"{Fore.RED}║          HUNG-TOOL HACK FREE FIRE 2025            ║{Fore.RESET}", delay=0.02)
    print_typing(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}", delay=0.02)
    select_user_id()
    
    while True:
        display_menu()
        print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] Nhập lựa chọn của bạn (1-3): {Fore.RESET}", end="")
        choice = input()

        if choice == "1":
            hack_diamonds()
        elif choice == "2":
            hack_coins()
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"Đang thoát tool... Cảm ơn bạn đã sử dụng!"
            )
            time.sleep(1)
            break
        elif choice == "4":
            get_game_name()
        elif choice in ["5", "6"]:
            error_message = random.choice(["Đang phát triển", "Kết nối server thất bại"])
            print(
                f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{error_message}]{Fore.RESET}"
            )
            time.sleep(1)
        else:
            print(
                f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 4."
            )

if __name__ == "__main__":
    main()

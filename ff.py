import random
import time
from datetime import datetime
import re
from colorama import init, Fore
import sys
import os

# Khởi tạo colorama
init()

# Biến toàn cục để lưu ID
user_id = ""

def print_typing(text, delay=0.05):
    """Hiệu ứng gõ chữ cho văn bản"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def get_user_info():
    global user_id
    while True:
        print(f"{Fore.YELLOW}Nhập ID game Free Fire (8-10 Số): {Fore.RESET}", end="")
        user_id = input()
        if re.match(r'^\d{8,12}$', user_id):
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"ID {Fore.CYAN}{user_id}{Fore.RESET} hợp lệ!"
            )
            time.sleep(1)
            break
        else:
            print(
                f"{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                f"{Fore.WHITE}-->>{Fore.RESET}"
                f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                f"ID {Fore.CYAN}{user_id}{Fore.RESET} không hợp lệ! ID Free Fire phải là 8-10 chữ số."
            )

def hack_diamonds():
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
    try:
        while True:
            diamonds = random.randint(0, 5)
            for countdown in range(20, -1, -1):  # Äáº¿m ngÆ°á»£c tá»« 3 Ä‘áº¿n 0
                print(
                    f"\r{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
                    f"{Fore.WHITE}-->>{Fore.RESET}"
                    f"{Fore.GREEN}[{countdown}]{Fore.RESET}"
                    f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
                    f"ID {Fore.CYAN}{user_id}{Fore.RESET} nhận được {Fore.WHITE}{diamonds} 💎 kim cương {Fore.RESET}",
                    end=""
                )
                sys.stdout.flush()  # Äáº£m báº£o in ngay láº­p tá»©c
                time.sleep(1)  # Chá» ~0.75 giĂ¢y Ä‘á»ƒ tá»•ng cá»™ng ~3 giĂ¢y cho 4 láº§n in
            print()  # Xuá»‘ng dĂ²ng sau khi Ä‘áº¿m ngÆ°á»£c xong
    except KeyboardInterrupt:
        print(
            f"\n{Fore.RED}[HUNG-TOOL]{Fore.RESET}"
            f"{Fore.WHITE}-->>{Fore.RESET}"
            f"{Fore.GREEN}[{datetime.now().strftime('%H:%M:%S')}]{Fore.RESET} "
            f"Đã dừng hack kim cương"
        )
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
        f"Nhập ID game Free Fire (8-10 chữ số): {Fore.RESET}",
        end=""
    )
    temp_id = input()
    time.sleep(1)
    if re.match(r'^\d{8,10}$', temp_id):
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
            f"ID {Fore.CYAN}{temp_id}{Fore.RESET} không hợp lệ! ID Free Fire phải là 8-10 chữ số."
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
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình
    print(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}")
    print_typing(f"{Fore.RED}║          HUNG-TOOL HACK FREE FIRE 2025            {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║ {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║Lưu ý: Đây là bản kết nối với server của mình.      {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║và đây cũng là bản test server nên kim cương  {Fore.RESET}", delay=0.03)
    print_typing(f"{Fore.RED}║hay là vàng sẽ về acc sau 24h {Fore.RESET}", delay=0.03)
    print(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}")
    print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M:%S')}] Người chơi: ID: {Fore.CYAN}{user_id}               {Fore.GREEN}Phiên bản: V1.2{Fore.RESET}")
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
        time.sleep(0.2)  # Hiệu ứng xuất hiện từng dòng

    print(f"{Fore.GREEN}└──────────────────────────────────────────────────────┘{Fore.RESET}")

def main():
    # Xóa màn hình và hiển thị tiêu đề ban đầu
    os.system('cls' if os.name == 'nt' else 'clear')
    print_typing(f"{Fore.RED}╔══════════════════════════════════════════════════════╗{Fore.RESET}", delay=0.02)
    print_typing(f"{Fore.RED}║          HUNG-TOOL HACK FREE FIRE 2025            ║{Fore.RESET}", delay=0.02)
    print_typing(f"{Fore.RED}╚══════════════════════════════════════════════════════╝{Fore.RESET}", delay=0.02)
    get_user_info()
    
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

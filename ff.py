import sys
import requests
import platform
import os
import time
from colorama import Fore, Style, init
import concurrent.futures

init(autoreset=True)

redeemed_or_exhausted_codes = set()

def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')

def prints(r, g, b, text="text", end="\n"):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m", end=end)

def animate_print(text, r_start, g_start, b_start, delay=0.0005, end=''):
    r, g, b = r_start, g_start, b_start
    for char in text:
        prints(r, g, b, char, end=end)
        time.sleep(delay)
        r = max(0, r - 5)
        g = max(0, g - 1)
        b = min(255, b + 5)
    print()

def banner():
    banner="""
░██████╗████████╗░██████╗░░██████╗░██╗░░░░░
██╔════╝╚══██╔══╝██╔═══██╗██╔═══██╗██║░░░░░
██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░
██║░░░░░░░░██║░░░██║░░░██║██║░░░██║██║░░░░░
╚██████╗░░░██║░░░╚██████╔╝╚██████╔╝███████╗
 ╚═════╝░░░╚═╝░░░░╚═════╝░░╚═════╝░╚══════╝
    """
    r = 255
    g = 255
    b = 255
    for i in banner.split('\n'):
        for j in i:
            prints(r, g, b, j, end='')
            time.sleep(0.0005)
            r-=5
            b-=1
        r = 255
        g = 255
        b = 255
        print()
    prints(247, 255, 97,"✨" + "═" * 45 + "✨")
    prints(32, 230, 151,"🌟 TOOL - NHẬP CODE 🌟".center(45))
    prints(247, 255, 97,"═" * 47)
    prints(7, 205, 240,"YouTube: https://www.youtube.com/@Tool-Xworld")
    prints(7, 205, 240,"Tiktok:https://www.tiktok.com/@cng1237929")
    prints(7, 205, 240,"Telegram: https://t.me/+PByWNy8hDxYzYTRl")
    prints(7, 205, 240,"Nhón zalo: https://zalo.me/g/fmyvre167")
    prints(7, 205, 240,"Admin: Thành Công | Zalo: 0842010239")
    prints(247, 255, 97,"═" * 47)


def theo_doi_code(code):
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'content-type': 'application/json',
        'country-code': 'vn',
        'origin': 'https://xworld-app.com',
        'priority': 'u=1, i',
        'referer': 'https://xworld-app.com/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
        'xb-language': 'vi-VN',
    }
    try:
        json_data = {
            'code': code,
            'os_ver': 'android',
            'platform': 'h5',
            'appname': 'app',
        }
        response = requests.post('https://web3task.3games.io/v1/task/redcode/detail', headers=headers, json=json_data).json()

        if response['code'] == 0 and response['message'] == 'ok':
            if 'data' in response and 'data' in response['data'] and 'admin' in response['data']['data']:
                sl = response['data']['data']['admin']['ad_show_value']
                loai = response['data']['currency']
                danhap = response['data']['progress']
                tong = response['data']['user_cnt']

                return tong - danhap
            else:
                prints(255, 165, 0, f'Warning: Unexpected response structure for code {code}: {response}', end='\n')
                return theo_doi_code(code)
        else:
            prints(255, 165, 0, f'API error for code {code}: {response.get("message", "Unknown error")}', end='\n')
            if "not exist" in response.get("message", "").lower():
                redeemed_or_exhausted_codes.add(code)
            return theo_doi_code(code)
    except requests.exceptions.RequestException as req_e:
        prints(255, 0, 0, f'Network error while tracking code {code}: {req_e}', end='\n')
        return theo_doi_code(code)
    except Exception as e:
        prints(255, 0, 0, f'Lỗi khi theo dõi code {code}: {e}', end='\n')
        return theo_doi_code(code)

def nhap_code(userId, secretKey, code):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
        'user-id': userId,
        'user-secret-key': secretKey,
        'xb-language': 'vi-VN',
    }
    try:
        json_data = {
            'code': code,
            'os_ver': 'android',
            'platform': 'h5',
            'appname': 'app',
        }
        response = requests.post('https://web3task.3games.io/v1/task/redcode/exchange', headers=headers, json=json_data).json()

        if response.get('code') == 0 and response.get('message') == 'ok':
            prints(0, 255, 250, f'[{userId}] Nhập code "{code}" thành công!', end='\n')
            prints(0, 255, 250, f'[{userId}] Nhận được {response["data"]["value"]:.2f} {response["data"]["currency"]}', end='\n')
            return True, "success"
        else:
            error_message = response.get('message', 'Unknown error')
            prints(255, 100, 0, f'[{userId}] Lỗi khi nhập code "{code}": {error_message}', end='\n')
            if "reward has been received" in error_message.lower() or "not exist" in error_message.lower():
                return nhap_code(userId, secretKey, code)
                return False, "exhausted_or_claimed"
            return False, error_message
    except requests.exceptions.RequestException as req_e:
        prints(255, 0, 0, f'[{userId}] Network error when redeeming code "{code}": {req_e}', end='\n')
        return nhap_code(userId, secretKey, code)
        return False, "network_error"
    except Exception as e:
        prints(255, 0, 0, f'[{userId}] Có lỗi khi nhập code "{code}": {e}', end='\n')
        return nhap_code(userId, secretKey, code)
        return False, "general_error"

def load_data_comfirm_codexw():
    user_ids = []
    user_secretkeys = []

    try:
        if os.path.exists('data_xw_confirm_code.txt'):
            x = input(Fore.YELLOW + 'Bạn có muốn sử dụng lại các thông tin tài khoản đã lưu không? (y/n): ' + Style.RESET_ALL).lower()
            if x == 'y':
                with open('data_xw_confirm_code.txt', 'r', encoding='utf-8') as f:
                    text = f.read()
                list_accounts = [line.strip() for line in text.split('\n') if line.strip()]
                for account_info in list_accounts:
                    parts = account_info.split('|')
                    if len(parts) == 2:
                        user_ids.append(parts[0])
                        user_secretkeys.append(parts[1])
                if user_ids:
                    prints(0, 255, 0, f'Đã lấy thành công thông tin {len(user_ids)} tài khoản: ')
                    prints(0, 255, 0, ", ".join(user_ids))
                    return user_ids, user_secretkeys
                else:
                    prints(255, 165, 0, "Không tìm thấy tài khoản hợp lệ trong tệp đã lưu. Vui lòng nhập mới.")

        prints(255, 255, 0, 'Nhập số lượng tài khoản bạn muốn dùng để nhập code:')
        num_accounts = int(input(Fore.CYAN + 'Số lượng tài khoản: ' + Style.RESET_ALL))

        for i in range(num_accounts):
            prints(218, 255, 125, "\n" + "=" * 10 + f" Hướng dẫn lấy link tài khoản {i+1} " + "=" * 10)
            prints(218, 255, 125, "1. Truy cập vào trang web xworld.io")
            prints(218, 255, 125, "2. Đăng nhập tài khoản của bạn")
            prints(218, 255, 125, "3. Tìm và nhấn vào 'Vua thoát hiểm' hoặc tương tự")
            prints(218, 255, 125, "4. Nhấn 'Lập tức truy cập'")
            prints(218, 255, 125, "5. Copy link trang web đó và dán vào đây")
            prints(247, 255, 97, "=" * 47)
            prints(125, 255, 168, f'📋Nhập link tài khoản {i+1}: ', end=' ')
            link = input()

            try:
                user_id_part = link.split('?userId=')[1].split('&')[0]
                secret_key_part = link.split('secretKey=')[1].split('&')[0]

                user_ids.append(user_id_part)
                user_secretkeys.append(secret_key_part)
                prints(0, 255, 0, f'Đã lấy dữ liệu thành công cho tài khoản {user_id_part}')
            except IndexError:
                prints(255, 0, 0, "Link không đúng định dạng. Vui lòng thử lại.")
                i -= 1

        if user_ids:
            with open('data_xw_confirm_code.txt', 'w', encoding='utf-8') as f:
                for i in range(len(user_ids)):
                    f.write(f'{user_ids[i]}|{user_secretkeys[i]}\n')
            prints(0, 255, 0, f'Đã lưu thông tin {len(user_ids)} tài khoản vào data_xw_confirm_code.txt')
        return user_ids, user_secretkeys

    except ValueError:
        prints(255,0,0,'Đầu vào không hợp lệ. Vui lòng nhập một số.')
        sys.exit(1)
    except Exception as e:
        prints(255,0,0,f'Lỗi khi lấy dữ liệu tài khoản: {e}')
        sys.exit(1)


def user_asset(userId, secretKey):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36',
        'user-id': userId,
        'user-secret-key': secretKey,
        'xb-language': 'vi-VN',
    }
    try:
        json_data = {
            'user_id': int(userId),
            'source': 'home',
        }

        response = requests.post('https://wallet.3games.io/api/wallet/user_asset', headers=headers, json=json_data).json()
        if response['code'] == 0 and response['msg']=='ok':
            asset = {
                'USDT': response['data']['user_asset'].get('USDT', 0),
                'WORLD': response['data']['user_asset'].get('WORLD', 0),
                'BUILD': response['data']['user_asset'].get('BUILD', 0)
            }
            return asset
        else:
            prints(255, 165, 0, f'Lỗi khi lấy số dư cho {userId}: {response.get("message", "Unknown error")}', end='\n')
            return None
    except requests.exceptions.RequestException as req_e:
        prints(255, 0, 0, f'Network error when getting balance for {userId}: {req_e}', end='\n')
        return None
    except Exception as e:
        prints(255, 0, 0, f'Lỗi khi lấy số dư cho {userId}: {e}', end='\n')
        return None

def print_wallet(asset, user_id):
    if asset:
        prints(247, 255, 97,"═" * 47)
        prints(238, 250, 7,f'SỐ DƯ CỦA TÀI KHOẢN {user_id}:')
        prints(23, 232, 159,f' USDT:{asset["USDT"]:.2f}    WORLD:{asset["WORLD"]:.2f}    BUILD:{asset["BUILD"]:.2f}'.center(50))
        prints(247, 255, 97,"═" * 47)
    else:
        prints(255, 0, 0, f'Không thể hiển thị số dư cho tài khoản {user_id}.')

def main_canh_code():
    banner()
    user_ids, user_secretkeys = load_data_comfirm_codexw()

    if not user_ids:
        prints(255,0,0,"Không có tài khoản nào được cấu hình. Thoát chương trình.")
        sys.exit(1)

    clear_screen()
    banner()

    codes = []
    try:
        t = int(input(Fore.YELLOW + 'Nhập số lượng giftcode cần theo dõi và nhập: ' + Style.RESET_ALL))
        for i in range(t):
            code_input = input(Fore.CYAN + f'Nhập giftcode thứ {i+1}: ' + Style.RESET_ALL).strip()
            if code_input:
                codes.append(code_input)

        if not codes:
            prints(255,0,0,"Không có giftcode nào được nhập. Thoát chương trình.")
            sys.exit(1)

        print(Fore.MAGENTA + """
        Ví dụ: Nếu giftcode của bạn đang có 300 lượt nhập,
        và bạn muốn đợi đến khi còn 50 lượt nhập (tức là 250/300 đã được nhập)
        thì bạn sẽ gõ 50.
        """ + Style.RESET_ALL)
        threshold = int(input(Fore.YELLOW + 'Số lượt nhập còn lại để tự động nhập giftcode: ' + Style.RESET_ALL))
    except ValueError:
        prints(255,0,0,'Đầu vào không hợp lệ. Vui lòng nhập một số.')
        sys.exit(1)

    clear_screen()
    banner()

    for i in range(len(user_ids)):
        asset = user_asset(user_ids[i], user_secretkeys[i])
        print_wallet(asset, user_ids[i])

    code_status = {code: None for code in codes}

    prints(247, 255, 97,"\n" + "═" * 47)
    prints(32, 230, 151,"BẮT ĐẦU THEO DÕI VÀ NHẬP CODE".center(45))
    prints(247, 255, 97,"═" * 47 + "\n")

    while True:
        current_time = time.strftime("%H:%M:%S")
        prints(173, 216, 230, f"[{current_time}] Đang theo dõi giftcode...", end='\r')
        sys.stdout.flush()

        all_codes_processed = True

        for code in list(codes):
            if code in redeemed_or_exhausted_codes:
                all_codes_processed = False
                continue

            remaining_entries = theo_doi_code(code)

            if remaining_entries is not None:
                code_status[code] = remaining_entries
                prints(255, 255, 0, f"[{current_time}] Code '{code}' còn {remaining_entries} lượt nhập.", end='\n')

                if remaining_entries <= threshold:
                    prints(0, 255, 100, f"[{current_time}] Đạt ngưỡng! Bắt đầu nhập code '{code}'...", end='\n')

                    with concurrent.futures.ThreadPoolExecutor(max_workers=len(user_ids)) as executor:
                        futures = []
                        for i in range(len(user_ids)):
                            future = executor.submit(nhap_code, user_ids[i], user_secretkeys[i], code)
                            futures.append(future)

                        success_count = 0
                        for future in concurrent.futures.as_completed(futures):
                            is_success, status_msg = future.result()
                            if is_success:
                                success_count += 1
                            elif status_msg == "exhausted_or_claimed":
                                redeemed_or_exhausted_codes.add(code)
                                prints(255, 165, 0, f"Code '{code}' đã hết lượt hoặc đã được nhận bởi tất cả tài khoản có thể. Sẽ không theo dõi nữa.", end='\n')
                                break

                        if success_count > 0:
                            prints(0, 255, 0, f"Tổng cộng {success_count} tài khoản đã nhập thành công code '{code}'.", end='\n')

                        final_remaining = theo_doi_code(code)
                        if final_remaining == 0:
                            redeemed_or_exhausted_codes.add(code)
                            prints(255, 165, 0, f"Code '{code}' đã được xác nhận là hết lượt. Sẽ không theo dõi nữa.", end='\n')
                        elif final_remaining is not None and final_remaining > 0:
                            prints(255, 255, 0, f"Code '{code}' vẫn còn {final_remaining} lượt sau khi nhập. Tiếp tục theo dõi.", end='\n')

            else:
                if code not in redeemed_or_exhausted_codes:
                     prints(255, 100, 0, f"[{current_time}] Không thể theo dõi code '{code}'. Có thể không hợp lệ hoặc đã hết hạn.", end='\n')
                     redeemed_or_exhausted_codes.add(code)

            if code not in redeemed_or_exhausted_codes:
                all_codes_processed = False

        if all_codes_processed and len(codes) > 0 and len(redeemed_or_exhausted_codes) == len(codes):
            prints(0, 255, 0, "Tất cả các giftcode đã được xử lý hoặc đã hết lượt. Thoát chương trình.")
            break
        elif len(codes) == 0:
            prints(255, 0, 0, "Không có giftcode nào để theo dõi. Thoát chương trình.")
            break

        time.sleep(1)

if __name__ == "__main__":
    main_canh_code()
# tam25107 codevip99 baothong01

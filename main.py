
import requests
from dotenv import load_dotenv
from utils.utils import claim_faucet
from utils.utils import get_random_proxy
from utils.utils import wait_until_next_interval
from display import appearance
from display import logging


load_dotenv()


def main():
    
    print(appearance.ASCII_ART)
    print(appearance.CREDIT)
    proxy = get_random_proxy()
    logging.log_info('-'*80)
    if proxy:
        logging.log_info("proxy found, processing with proxy")
        claim_faucet(proxy)
    else:
        logging.log_warning("proxy not found, processing directly")
        claim_faucet()
   


if __name__ == "__main__":
    while True:
        main()
        wait_until_next_interval()
        continue

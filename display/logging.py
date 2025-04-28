from colorama import Fore, Style
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def log_info(message):
    print(f"{Fore.CYAN}{Style.NORMAL}[INFO] {message}{Style.RESET_ALL}")

def log_success(message):
    print(f"{Fore.GREEN}{Style.NORMAL}[SUCCESS] {message}{Style.RESET_ALL}")

def log_warning(message):
    print(f"{Fore.YELLOW}{Style.NORMAL}[WARNING] {message}{Style.RESET_ALL}")

def log_error(message):
    print(f"{Fore.RED}{Style.NORMAL}[ERROR] {message}{Style.RESET_ALL}")

def log_debug(message):
    print(f"{Fore.MAGENTA}{Style.NORMAL}[DEBUG] {message}{Style.RESET_ALL}")

def log_critical(message):
    print(f"{Fore.RED}{Style.BRIGHT}[CRITICAL] {message}{Style.RESET_ALL}")

def log_trace(message):
    print(f"{Fore.CYAN}{Style.DIM}[TRACE] {message}{Style.RESET_ALL}")

def log_fatal(message):
    print(f"{Fore.BLACK}{Style.BRIGHT}[FATAL] {message}{Style.RESET_ALL}")

def log_ask(message):
    print(f"{Fore.BLUE}{Style.NORMAL}[ASK] {message}{Style.RESET_ALL}")

def log_update(message):
    print(f"{Fore.YELLOW}{Style.NORMAL}[UPDATE] {message}{Style.RESET_ALL}")
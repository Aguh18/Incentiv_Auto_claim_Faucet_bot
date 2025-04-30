# Incentiv Testnet Faucet Claimer Bot

## Overview
The **Incentiv Testnet Faucet Claimer Bot** is a simple Python tool to automate claiming tokens from the `testnet.incentiv.net` faucet every 4 hours. 

## Features
- Automatic faucet claiming.
- Proxy support.

## Prerequisites
- **Python 3.8+**.
- **2Captcha account** with an API key.
- (Optional) Proxies for anonymous requests.

## Installation
1. **Get the Code**  
   Clone or create a folder for the code:
   ```bash
   git clone https://github.com/Aguh18/Incentiv_Auto_claim_Faucet_bot.git
   cd Incentiv_Auto_claim_Faucet_bot.git
   ```
   

2. **Set Up Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Tools**  
   Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Configuration**  
   Create a `.env` file in the project folder:
   ```env
   TWOCAPTCHA_API_KEY=your_2captcha_api_key
   TOKEN=your_faucet_token
   SITE_KEY=your_turnstile_site_key
   ```
   - `TWOCAPTCHA_API_KEY`: Your 2Captcha API key.
   - `TOKEN`: Bearer token from `testnet.incentiv.net`.
   - `SITE_KEY`: Turnstile site key from the faucet website 

5. **(Optional) Set Up Proxies**  
   Proxy usage is optional. To use proxies, create a `proxies.txt` file in the project folder with proxies in one of these formats:
   ```
   username:password@host:port
   host:port
   protocol://host:port
   protocol://username:password@host:port
   ```
   Example:
   ```
   user:pass@192.168.1.1:8080
   192.168.1.2:8888
   socks5://10.0.0.1:9999
   socks5://user:pass@10.0.0.1:9999
   ```

## Usage
1. **Check Setup**  
   Ensure `.env` is configured and 2Captcha has funds. If using proxies, verify `proxies.txt`.

2. **Run Bot**  
   ```bash
   python main.py
   ```


## Safety Tips
- Don’t share your `.env` file or 2Captcha API key.
- Verify proxy sources for security.
- Check code before adding sensitive data.
`.

## Disclaimer
For educational use only. Use at your own risk. Creators are not liable for issues any issues
## License
MIT License

## Community

- [AutoDropz Telegram](https://t.me/+V_JQTTMVZVU3YTM9)
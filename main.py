import requests
import time

BOT_TOKEN = "8579945497:AAG2rxeNscB9mo--d2F1l3dWvwqiUlFuEz8"
ADMIN_ID = "8207126990"
LAST_MINT = ""

def check_pump():
    global LAST_MINT
    url = "https://frontend-api.pump.fun/coins?offset=0&limit=5&sort=created_timestamp&order=DESC"
    try:
        data = requests.get(url, timeout=10).json()
        if data and data[0]['mint'] != LAST_MINT:
            LAST_MINT = data[0]['mint']
            tg = data[0].get('telegram', '')
            if tg and "t.me" in tg:
                msg = f"🚀 *TG DETECTED*\n\nName: {data[0]['name']}\n[Join TG]({tg})"
                requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", 
                              json={"chat_id": ADMIN_ID, "text": msg, "parse_mode": "Markdown"})
    except:
        pass

if __name__ == "__main__":
    while True:
        check_pump()
        time.sleep(10)

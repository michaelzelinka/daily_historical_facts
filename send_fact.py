import os
import json
import random
import requests

FACT_FILE = "facts.txt"
SENT_FILE = "sent.json"


def load_facts():
    with open(FACT_FILE, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def load_sent():
    if not os.path.exists(SENT_FILE):
        return []
    with open(SENT_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except:
            return []


def save_sent(sent):
    with open(SENT_FILE, "w", encoding="utf-8") as f:
        json.dump(sent, f, ensure_ascii=False, indent=2)


def send_discord_message(msg):
    webhook = os.getenv("DISCORD_WEBHOOK")
    if not webhook:
        print("❌ Missing DISCORD_WEBHOOK")
        return

    resp = requests.post(webhook, json={"content": msg})
    print("✅ Discord status:", resp.status_code)


if __name__ == "__main__":
    facts = load_facts()
    sent = load_sent()

    available = [f for f in facts if f not in sent]

    if not available:
        send_discord_message("✅ All facts have been sent! Please add more 😊")
        exit(0)

    fact = random.choice(available)
    
    day_number = len(sent) + 1
    total_facts = len(facts)
    
    message = (
        f"📜 **Daily historical fact** ({day_number}/{total_facts})\n\n"
        f"{fact}"
    )
    
    send_discord_message(message)
    
    sent.append(fact)
    save_sent(sent)
    

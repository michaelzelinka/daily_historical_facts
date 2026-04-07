# 📜 Daily Historical Facts Bot

A simple and fully automated GitHub Actions bot that sends **one interesting historical fact per day** to a Discord channel.

The goal of this project is not productivity or performance, but perspective:
a short daily reminder that life in the modern world is, in many ways, remarkably comfortable compared to the past.

---

## ✨ What This Bot Does

- 🕖 Runs once per day using a GitHub Actions cron job
- 📜 Selects one historical fact from a predefined list
- 🔁 Ensures facts are **never repeated**
- 🤖 Sends the fact automatically to a Discord channel
- 💾 Persists state (`sent.json`) to keep track of already sent facts
- ✅ Requires no maintenance after setup

---

## 📦 Project Structure

``
.
├── facts.txt        # List of historical facts (one per line)
├── sent.json        # Tracks which facts were already sent
├── send_fact.py     # Main Python script
└── .github
└── workflows
└── daily.yml   # GitHub Actions cron workflow

---

## 🧠 Philosophy

This project intentionally avoids complexity:

- ❌ No scraping
- ❌ No databases
- ❌ No AI
- ❌ No external dependencies beyond a webhook

It is a **small, reliable automation** designed to quietly run in the background
and deliver something interesting every morning.

---

## 📨 Example Discord Message

📜 Daily historical fact:
In ancient Mesopotamia, workers were often paid in beer.

---

## 🔧 Setup Overview

### 1. Discord Webhook
Create a Discord webhook for the channel where messages should be sent.


### 2. GitHub Secret
Add the webhook URL as a repository secret:
DISCORD_WEBHOOK


### 3. Facts List
Populate `facts.txt` with historical facts.
Each line represents one fact.


Example:

🍺 In ancient Mesopotamia, workers were often paid in beer.
🦷 The first dental drill dates back to 7000 BCE.
🚿 In medieval Europe, people feared baths caused illness.


### 4. Initial State
Create a `sent.json` file with the following content:

```json
[]
```

## 5. Schedule
The bot runs daily using GitHub Actions and a cron schedule.
The cron time is based on UTC, so adjust accordingly for your local timezone.


## ✅ Why This Exists

To bring context into everyday life
To reduce doom‑scrolling with historical perspective
To prove that small automation projects can still be meaningful
To create something that finishes, not something that grows endlessly


## 🚀 Possible Extensions (Optional)

Weekly summaries
Category tagging (medicine, politics, technology, culture)
Weekend‑specific messages
Email delivery instead of Discord
Quote + historical fact combo

All intentionally left out of the core project to keep it simple.

## 📜 License
MIT — free to use, modify, or adapt for your own daily reminders.


Sometimes the most valuable projects are the ones that quietly work,
do one thing well, and never demand attention again.

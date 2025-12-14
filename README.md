# 🤖 Mention Network Automation Bot (Premium Edition)

![Python Version](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-Proprietary-red)
![Status](https://img.shields.io/badge/Status-Active-success)

A high-performance, multi-threaded automation tool designed for **Mention Network**. This bot utilizes advanced AI models (Gemini/Groq) to generate organic, context-aware conversations, manage daily quests, and maximize point farming efficiency.

> **🔒 Security Note:** This project includes advanced security features and obfuscation methods to protect core logic.
<img width="752" height="361" alt="image" src="https://github.com/user-attachments/assets/25a2d5b2-ffe4-47fa-b864-8be6f775b8ab" />

---

## ✨ Key Features

* **🧠 Advanced AI Integration:** Uses Google Gemini & Groq (Llama 3) to generate human-like answers.
* **🎭 Smart Persona System:** Automatically generates unique personas with specific interests and traits to avoid detection.
* **⚡ Multi-Threaded:** Runs multiple accounts simultaneously with optimized delay handling.
* **🛡️ Strict Proxy Support:** Secure connection management with IP rotation support.
* **📱 Telegram Control Center:** Monitor status, add keys, and control the bot remotely via Telegram.
* **🔄 Smart Recovery:** Auto-sleeps and resumes when API limits are reached (50-minute cool-down).
* **⚔️ Auto Quests:** Automatically completes "Visit" and "Follow" quests.

---

## ✅ System Requirements (IMPORTANT)
To use this bot, you MUST install `Python 3.11`.
Other versions (like 3.10 or 3.12) will NOT work because the core engine is compiled specifically for version 3.11.

### ⚠️ Required:
- Python 3.11.x (64-bit)
- Windows 10/11
- License Activation : https://form.jotform.com/253471232172046
---

## 🚀 Installation
### 1. Clone the Repository
```Bash
git clone https://github.com/genoshide/mention-network-bot.git
cd mention-network-bot
```
### 2. Create a Virtual Environment
It is recommended to use a virtual environment to avoid conflicts.
#### Windows
```Bash 
python -m venv venv
```
```bash
venv\Scripts\activate
```

#### Linux/Mac
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
### 3. Install Dependencies
```Bash
pip install -r requirements.txt
```

## ⚙️ Configuration
Before running the bot, you must configure the files inside the data/ folder.

### 1. data/token.txt
Paste your Mention Network JWT tokens here (one per line).
```Plaintext
eyJhbGciOiJIUzI1NiIsIn...
eyJhbGciOiJIUzI1NiIsIn...
```
### 3. data/proxy.txt
Add your proxies in http format (one per line). 
Required if USE_PROXY = True.
```Plaintext
user:pass@ip:port
user:pass@ip:port
```
### 4. data/api.txt
Add your AI API Keys (Google Gemini or Groq). The bot will rotate them automatically.
```Plaintext
AIzaSyD...  (Gemini)
gsk_8Ja...  (Groq)
```
### 5. Configuration's (Optional)
Rename `.env.example` to `.env` ou can adjust settings like thread count, delays, and Telegram credentials here.
```yaml
CHAT_COUNT_MIN=5
CHAT_COUNT_MAX=15

SLEEP_BETWEEN_CYCLES_MIN=300
SLEEP_BETWEEN_CYCLES_MAX=600

THREADS=3
USE_PROXY=false
HUMAN_TYPING=false
AUTO_COMPLETE_QUESTS=false
SMART_CONVERSATION=false

START_DELAY_MIN=5
START_DELAY_MAX=15
DELAY_MIN=5
DELAY_MAX=10
SLEEP_WHEN_API_LIMIT=10

USE_TELEGRAM=false
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
TELEGRAM_ALLOWED_IDS=
```

## 🖥️ Usage
Once configured, simply run:
```Bash
python main.py
```
The bot will perform a license check, validate your configuration files, and start the mining threads.

---

## Real-time Interaction
Manage your bot remotely without touching the server. The bot includes a complete command menu.

> *Example: Adding a Groq API key via Telegram triggers an immediate update on the server log.*


### 📡 Telegram Commands
If `USE_TELEGRAM = True`, you can control the bot via your private bot.
| Command | Description |
| :--- | :--- |
| `/status` | View live points, running threads, and license status. |
| `/logs` | Fetch the last 15 lines of terminal logs. |
| `/screenshot` | Capture a screenshot of the server/VPS. |
| `/add_token` | Add a new account token remotely. |
| `/add_api` | Add a new AI API Key remotely. |
| `/stop` | Force shutdown the bot. |
| `/restart` | Restart the bot process. |

## 🖥️ Dashboard Interface

The bot features a rich terminal UI (TUI) that displays real-time statistics, worker threads, and AI logs.

> *Real-time monitoring showing active threads, AI responses, and point accumulation.*

## 📂 Directory Structure

```text
mention-bot/
├── data/
│   ├── token.txt       # List of Account JWT Tokens
│   ├── proxy.txt       # List of Proxies (user:pass@ip:port)
│   ├── api.txt         # Gemini/Groq API Keys
│   └── personas.json   # Generated AI Characters (Do not edit manually)
├── src/
│   ├── starter.pyd     # Compiled Core Logic (Protected)
│   └── ...
├── main.py             # Entry point (Loader)
├── requirements.txt    # Python dependencies
├── PRODUCT_INFO.txt    # Genoshide Mention Network Bot Informations
└── README.md
```

## ⚠️ Disclaimer
This tool is for educational purposes only. The developer is **not responsible** for any bans or penalties applied to your Mention Network accounts. Use this tool at your own risk.

## 📜 License
**Copyright © 2025 Genoshide**. All rights reserved.Unauthorized **copying**, **modification**, or **distribution** of this file, via any medium, is strictly prohibited.
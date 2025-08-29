# botASS

A Python bot that sends assembler exercises generated with Google GenAI, directly by mail.

--------

## Installation

```bash
git clone https://github.com/ton-user/botASS.git
cd botASS

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
mv template.env .env

# Initialize the database
python scripts/manage_db.py
```

### Setup the .env with your infomations

```ini
# API
API_KEY=your_gemini_api_key
MAX_TOKEN=500

# MAIL BOT
BOT_MAIL=bot_mail@exemple.com
BOT_MAIL_PASSWD=bot_mail_passwd

# MAIL TARGET
TARGET_MAIL=your_mail@exemple.com

# DB PATH
DB_PATH=./data/botASS.db
```

--------

## Run
```bash
python -m bot.main
```

--------

## Automate with cron (Linux)

You can set up a daily training with  cron :
```cron
0 8 * * * cd ~/botASS && python -m bot.main >> logs/cron.log 2>&1
```
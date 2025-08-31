# botASS

A Python bot that sends assembler exercises generated with Google GenAI, directly by mail.

--------

## Installation

Clone the repository :
```bash
git clone https://github.com/Allu-mette/botASS.git
cd botASS
```

I recommend using a Python virtual environment (venv) :
```bash
python -m venv env
# Linux
source ./env/bin/activate
# Windows
env\Scripts\activate
```

Then run :
```bash
# Install dependencies
pip install -r requirements.txt

# Copy environment variables
mv template.env .env

# Initialize the database
python scripts/manage_db.py create
```

### Setup the .env with your informations

```ini
# API
API_KEY=your_gemini_api_key
MAX_TOKEN=500

# MAIL BOT
BOT_MAIL=bot_mail@example.com
BOT_MAIL_PASSWD=bot_mail_passwd

# MAIL TARGET
TARGET_MAIL=your_mail@example.com
```

--------

## Run
```bash
python -m bot.main
```

--------

## Automate with cron

You can set up a daily training with  cron (Linux) :

`0 8 * * * cd ~/botASS && python -m bot.main >> cron.log 2>&1`

--------

## Edit the prompt file to customize the exercises
`bot/prompt.txt`

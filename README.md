# New-World-Server-Status-Scraper-DE

Forked Discord bot of https://github.com/40Cakes/New-World-Server-Status-Scraper

Added features : 
- Localized in French
- Add maintenance Status

 Requirements:
-  python
-  pip

Install script dependencies:
```
pip install -r requirements.txt
```

Update the Discord webhook URL variable in server_status.py to post to that channel or create a WEBHOOK_URL config variable.

Schedule script to run every x minutes (cron):
```
python3 server_status.py
```

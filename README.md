# New-World-Server-Status-Scraper-DE

## Added features

- Localized in German
- Add maintenance Status

## Requirements

- python
- pip

### Install script dependencies

```python
pip install -r requirements.txt
```

Update the Discord webhook URL variable in server_status.py to post to that channel or create a file named `config.env` with WEBHOOK_URL config variable.

Schedule script to run every x minutes (cron)

```
python3 server_status.py
```

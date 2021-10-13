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

Update the Discord webhook URL variable in server_status.py to post to that channel or create a ENVIRONMENT variable named WEBHOOK_URL.

Schedule script to run every x minutes (cron) or use github actions. (If using github actions you need to create a actions secret `secrets.WEBHOOK_URL`)

```python
python3 server_status.py
```

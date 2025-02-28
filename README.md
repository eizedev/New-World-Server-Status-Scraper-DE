[![New World Server status](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/python-app-run.yml/badge.svg)](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/python-app-run.yml) [![Python application testing/linting](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/python-app-test.yml/badge.svg)](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/python-app-test.yml) [![CodeQL](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/eizedev/New-World-Server-Status-Scraper-DE/actions/workflows/codeql-analysis.yml) 

![New World](https://user-images.githubusercontent.com/6794362/143776026-a48c2968-d3ea-4b82-8a17-88173efd74ce.jpg)

# New World Server Status Scraper

Parses the [New World Server Status page](https://www.newworld.com/support/server-status) and will sent a message to a defined Discord channel (Webhook) if server status changes.

If using the github actions files, the check will run every 5 minutes.

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

## Disclaimer

> The scripts in this repository fetches data from the [official New World website]((https://www.newworld.com/support/server-status)). So this mechanism can break any time without any notice if Amazon Game Studios make any structure change on their server status page.

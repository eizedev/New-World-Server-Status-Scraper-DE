from bs4 import BeautifulSoup
from functions import deep_diff
from functions import switch
import requests
import json
from dotenv import load_dotenv
import os
import logging

##########
# CONFIG #
##########

load_dotenv()

scrape_url = "https://www.newworld.com/fr-fr/support/server-status"
webhook_url = os.environ.get('WEBHOOK_URL')

filter_regions = True # Set to True to only post updates about certain regions
monitored_regions = ["Eu Central"] # List of regions to update

filter_servers = True # Set to True to only post updates about certain servers
monitored_servers = ["Thrudheim", "Mandara", "Lacerta"] # List of server to update

logging.basicConfig(format='%(message)s', level="INFO")
log = logging.getLogger('root')

region_index = 0
regions_dict = {}
servers_dict = {}
new_status_dict = {}

page = requests.get(scrape_url)

filename = "status.json"
if os.path.isfile(filename):
    log.info("Found file: status.json, loading previous server statuses...")
    no_prev_status_dict = False
    with open(filename,'r') as file:
        prev_status_dict = eval(file.read())
else:
    log.info("No file found: status.json, setting script to initialize status.json...")
    no_prev_status_dict = True

log.info("Attempting to scrape URL: " + scrape_url)
scrape = BeautifulSoup(page.content, "html.parser")

log.info("Getting server status section of page...")
status_section = scrape.find("section", {"class": "ags-ServerStatus ags-l-backgroundArea"})

log.info("Getting list of server regions from page...")
regions = status_section.find_all("a", class_="ags-ServerStatus-content-tabs-tabHeading")

for region in regions:
    region_name = region.find("div", class_="ags-ServerStatus-content-tabs-tabHeading-label")
    regions_dict[region_index] = region_name.text.strip()
    log.info("Found region on page: " + region_name.text.strip())

    new_status_dict[region_name.text.strip()] = {}
    region_index += 1

log.info("Getting list of servers in each region...")
for index, region in regions_dict.items():

    regions_server = status_section.find_all("div", class_="ags-ServerStatus-content-responses-response")[index]
    servers = regions_server.find_all("div", class_="ags-ServerStatus-content-responses-response-server")

    for server in servers:
        server_name = server.find("div", class_="ags-ServerStatus-content-responses-response-server-name")

        if server.find_all("div", {"class": "ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--up"}):
            server_status = "✅"
        elif server.find_all("div", {"class": "ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--down"}):
            server_status = "❌"
        elif server.find_all("div", {"class": "ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--full"}):
            server_status = "🔒"
        elif server.find_all("div", {"class": "ags-ServerStatus-content-responses-response-server-status ags-ServerStatus-content-responses-response-server-status--maintenance"}):
            server_status = "🔧"
        else:
            server_status = "💨"

        log.info(server_status + " - " + region + ", " + server_name.text.strip())
        new_status_dict[region].update({server_name.text.strip() : server_status})

log.info("\nWriting new server statuses to file: status.json...")
with open(filename, 'w') as file:
    file.write(json.dumps(new_status_dict))
    if no_prev_status_dict:
        prev_status_dict = dict(new_status_dict)

log.info("Checking differences between previous server statuses and current statuses...")
diff = deep_diff(prev_status_dict, new_status_dict)

if diff != None:
    log.info("Server status changes detected!")

    diff_json = json.dumps(diff)
    diff_dict = json.loads(diff_json)

    for region in diff_dict:
        for server in diff_dict[region]:
            
            old_status = "null"
            if diff_dict[region][server][0]:
                old_status = diff_dict[region][server][0]
                
            new_status = diff_dict[region][server][1]

            log.info(region + ", " + server + "\nPrevious State: " + old_status + " - Current State: " + new_status)

            if filter_servers:
                if server in monitored_servers:
                    switch(old_status, new_status, webhook_url, region, server, scrape_url)
            elif filter_regions:
                if region in monitored_regions:
                    switch(old_status, new_status, webhook_url, region, server, scrape_url)
            else:
                switch(old_status, new_status, webhook_url, region, server, scrape_url)
else:
    log.info("No server status changes detected!")
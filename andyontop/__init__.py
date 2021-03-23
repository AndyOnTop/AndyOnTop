import subprocess
import requests
from dhooks import Webhook
import json
from time import sleep
import asyncio

# Get HWID
def get_hwid():
    hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
    return hwid

# Get IP
def get_ip():
    query = requests.get("https://wtfismyip.com/text").text
    return query

# IP lookup
def geo_location(ip):
    query = requests.get(f"https://ipapi.co/{ip}/json").text
    return query

# Convert text to ASCII
def ascii(text):
    query = requests.get(f"https://artii.herokuapp.com/make?text={text}").text
    return query

# Change Webhook Name
def webhook_name(name, webhook_url):
    webhook = Webhook(webhook_url)
    webhook.modify(name=name)

# Webhook Delete
def webhook_delete(webhook_url):
    webhook = Webhook(webhook_url)

    webhook.delete()

# Webhook Spammer
def webhook_spammer(webhook_url, message):
    hook = Webhook(webhook_url)
    info = hook.default_name
    while True:
        hook.send(message)
        print("Sent " + message)
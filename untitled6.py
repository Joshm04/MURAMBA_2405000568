# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RrT7SFQ5a2ThSvexkrYUezchuYPNrmHE
"""

import requests
def check_website(url):
   try:
       response=requests.get(url ,timeout=5)
       return f"website {url} is up (status:{response.status_code})"
   except requests.exceptions.RequestException:
       return f"website{url} is unreachable"
print(check_website("https://uok.ac.rw"))

import requests
import smtplib
from email.mime.text import MIMEText
import logging
import time

logging.basicConfig(filename='website_status.log', level=logging.INFO)

def send_email(subject, body, to):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "edgarbahati@gmail.com"
    msg['To'] = to

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login("your_email@example.com", "your_password")
        server.send_message(msg)

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return f"Website {url} is up (status: {response.status_code})"
    except requests.exceptions.RequestException as e:
        logging.error(f"Website {url} is unreachable: {e}")
        send_email("Website Down", f"Website {url} is unreachable: {e}", "recipient@example.com")
        return f"Website {url} is unreachable"

urls = ["https://uok.ac.rw"]

iterations =4

for i in range(iterations):
    for url in urls:
        print(check_website(url))
    time.sleep(3)
#!/usr/bin/env python3

import psutil
import email
"""
Checks system health
"""

def send_error_report(sender, recipient, subject, body):
        message = email.generate_email(sender, recipient, subject, body)
        email.send_email(message)


def main():
    sender = "automation@example.com"
    recipient = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    if psutil.cpu_percent(interval=1) > 80 :
        subject = "Error - CPU usage is over 80%"
        send_error_report(sender, recipient, subject, body)
    
    if psutil.disk_usage("/").free < (psutil.disk_usage("/").total * 0.2) :
        subject = "Error - Available disk space is less than 20%"
        send_error_report(sender, recipient, subject, body)

    if psutil.virtual_memory().available < (500*1024*1024):
        subject = Error - "Available memory is less than 500MB"

main()
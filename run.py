# python native imports
import os
import sys
import time
import requests
import logging

# third party imports
import google.cloud.logging
from twilio.rest import Client


# environment setup 
LOG_LOCAL      = os.environ.get("LOG_LOCAL", False) 
INTERVAL_SEC   = os.environ.get("INTERVAL_SEC", 60)
ACCOUNT_SID    = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN     = os.environ.get("AUTH_TOKEN")
SENDER_PHONE   = os.environ.get("SENDER_PHONE")
RECEIVER_PHONE = os.environ.get("RECEIVER_PHONE")
URL_REG        = os.environ.get("URL_REG")
URL_TEST       = os.environ.get("URL_TEST")
URL_WARNING    = os.environ.get("URL_WARNING")

awe_reg_message = "Black hat Advanced Windows \
Exploitation \registration is online. Visit \
https://www.blackhat.com/us-23/training/schedule to register now!"

awe_test_message = "This is a test message to \
validate that twilio is successfully configured. \
You will receive a message from the bot when course \
registration becomes available."

awe_warning_message = "The Advanced Windows Exploitation \
Black Hat notification tool received an unexpected status \
code from the website. You should check out the tool and \
website to see if something is broken or if the course is \
about to go live. The tool will continue to run just in \
case the course is about to go live."


# logging configuration, local or remote
if LOG_LOCAL:
    logging.basicConfig(stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

else: google.cloud.logging.Client().setup_logging()


# twilio client establishment
client = Client(ACCOUNT_SID, AUTH_TOKEN)


# twilio action wrappers
def send_text_message(message_content:str) -> str:
    return client.messages.create(
        to=RECEIVER_PHONE,
        from_=SENDER_PHONE,
        body=message_content
    ).sid

def make_phone_call(content_url:str) -> str:
    return client.calls.create(
        to=RECEIVER_PHONE,
        from_=SENDER_PHONE,
        url=content_url
    ).sid


# send test cases to verify tool is successfully configured
logging.info(f"sending test cases to validate that the tool is successfully configured")
logging.info(f"executing a text message to user, status code '{send_text_message(awe_test_message)}'")
logging.info(f"executing a phone call to user, status code '{make_phone_call(URL_TEST)}'")


sequential_fail_count = 0

# run the test case until it hits
while True:
    registration_status_code = requests.get("https://www.blackhat.com/us-23/training/schedule/").status_code
    logging.info(f"website tested, returned status code: {registration_status_code}")

    # check if course registration is live
    if registration_status_code == 200:
        logging.info(f"the tool received a 200 from the website, registration is likely live")
        logging.info(f"executing a text message to user, status code '{send_text_message(awe_reg_message)}'")
        logging.info(f"executing a phone call to user, status code '{make_phone_call(URL_REG)}'")

        # we're done, hope you got a seat
        logging.info(f"we're done, hope you got a seat... holding indefinitely to prevent reboot'")
        time.sleep(60*60*24*365) # 1 year

    # something unexpected happened, check the tool, will continue executing just in case
    elif registration_status_code != 404:
        sequential_fail_count += 1

        if sequential_fail_count > 5:
            logging.warning(f"the tool received an unexpected status code {registration_status_code}")
            logging.warning(f"executing a text message to user, status code '{send_text_message(awe_warning_message)}'")
            logging.warning(f"executing a phone call to user, status code '{make_phone_call(URL_WARNING)}'")
            logging.warning(f"this is the {sequential_fail_count} sequential non--404 received, something bad is happening")

    # normal 404 recieved, reset failure counter
    else: sequential_fail_count = 0


    # wait to re-test status
    time.sleep(INTERVAL_SEC)
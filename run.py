#!/usr/bin/python3

# library imports
import os, sys, time, requests, logging, google.cloud.logging
from twilio.rest import Client

# logging configuration
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="auth.json"

google_log_client = google.cloud.logging.Client()
google_log_client.setup_logging()

logging.basicConfig(stream=sys.stdout,
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')


# globals 
DELAY = 60 # in seconds
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
from_phone_number = os.environ['TWILIO_FROM_PHONE_NUMBER']
to_phone_number = os.environ['TWILIO_TO_PHONE_NUMBER']


# twilio client establishment
client = Client(account_sid, auth_token)



# twilio action wrappers
def send_text_message(message_content:str) -> str:
    return client.messages.create(
        body=message_content,
        from_=from_phone_number,
        to=to_phone_number
    ).sid


def make_phone_call(content_url:str) -> str:
    return client.calls.create(
        url=content_url,
        from_=from_phone_number,
        to=to_phone_number
    ).sid


awe_reg_message = "Black hat Advanced Windows Exploitation registration is online. Visit https://www.blackhat.com/us-23/training/schedule to register now!"
awe_test_message = "This is a test message to validate that twilio is successfully configured. You will receive a message from the bot when course registration becomes available."
awe_warning_message = "The Advanced Windows Exploitation Black Hat notification tool received an unexpected status code from the website. You should check out the tool and website to see if something is broken or if the course is about to go live. The tool will continue to run just in case the course is about to go live."

awe_reg_url = "https://handler.twilio.com/twiml/EH923e23e88b7be9d5cac065342bf323e7"
awe_test_url = "https://handler.twilio.com/twiml/EHae0b918431d9218ab8e1d13dedbf8aae"
awe_warning_url = "https://handler.twilio.com/twiml/EHca803ad458b7437ca271794fd0534660"


# send test cases to verify tool is successfully configured
logging.info(f"sending test cases to validate that the tool is successfully configured")
logging.info(f"executing a text message to user, status code '{send_text_message(awe_test_message)}'")
logging.info(f"executing a phone call to user, status code '{make_phone_call(awe_test_url)}'")


# run the test case until it hits
while True:
    registration_status_code = requests.get("https://www.blackhat.com/us-23/training/schedule/").status_code
    logging.info(f"website tested, returned status code: {registration_status_code}")

    # check if course registration is live
    if registration_status_code == 200:
        logging.info(f"the tool received a 200 from the website, registration is likely live")
        logging.info(f"executing a text message to user, status code '{send_text_message(awe_reg_message)}'")
        logging.info(f"executing a phone call to user, status code '{make_phone_call(awe_reg_url)}'")

        # we're done, hope you got a seat
        break

    # something unexpected happened, check the tool, will continue executing just in case
    elif registration_status_code != 404:
        logging.warning(f"the tool received an unexpected status code {registration_status_code}")
        logging.warning(f"executing a text message to user, status code '{send_text_message(awe_warning_url)}'")
        logging.warning(f"executing a phone call to user, status code '{make_phone_call(awe_warning_url)}'")

    # wait to re-test status
    time.sleep(DELAY)
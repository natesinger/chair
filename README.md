# Chair
Chair is a python both that makes requests to the blackhat training page and when the page 200's it notifies the target phone number via sms and phone call.

## Image Build Process
1. Navigate to the root of this repository
2. Run ```docker build . -t awe-notification-bot```
3. Push the image to the repository of whatever cloud provider you're using

## Runtime Environment
This tool requires four environment variables to be set in order to execute. These variables provide the tool with enough context to reach out to your specific Twilio account as well as the information it needs to send messages and makes calls to the right phone number.

Recommend setting up twilio with recurring billing in case it runs out

### Twilio SID
SID stands for String Identifier. It's a unique key that is used to identify specific resources. At Twilio, each SID has 34 digits and you can identify the type of SID and the product it's associated with by the first two characters. Your Twilio SID can be retrieved from the console located at https://console.twilio.com/.

```TWILIO_ACCOUNT_SID="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"```

### Twilio Authentication Token
Twilio uses two credentials to determine which account an API request is coming from: The Account SID, which acts as a username, and the Auth Token which acts as a password. This guide explains how to find your Auth Token, and how to change it.

```TWILIO_AUTH_TOKEN="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"```

### FROM and TO Phone Numbers
Twilio uses two phone numbers to execute sms messages and calls. The FROM phone number is going to be from the device you setup in Twilio. This is a critical step and can be accomplished from the console. If you dont have the correct FROM number the messages and calls will not succeed. The TO number is your phone that you want to be notified on.

```TWILIO_FROM_PHONE_NUMBER="+14567891234"```<br>
```TWILIO_TO_PHONE_NUMBER="+14567891234"```

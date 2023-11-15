# Chair
Chair is a python both that makes requests to the blackhat training page and when the page 200's it notifies the target phone number via sms and phone call. The image will send an initial test message and perform a test call when you set it up. If it doesn't do this something is probably wrong.

# Contributors
## Nate Singer
#### nathaniel\<at\>singer\<dot\>cloud
I wrote this bot to take a shot at a Blackhat AWE seat for the --2023--2024 offering. Results to be determined but you are welcome to take advantage of this tool or fork/pull additional features as you'd like.

# Artifact Build & Execution

## Image Assembly & Push
1. Retrieve an authentication token and authenticate your Docker client to your registry. Use the AWS CLI:<br>
```aws ecr get-login-password --region us-west-1 | docker login --username AWS --password-stdin 012672079470.dkr.ecr.us-west-1.amazonaws.com```

2. Build your Docker image using the following command. For information on building a Docker file from scratch see the instructions here . You can skip this step if your image is already built:<br>
```docker build -t chair .```

3. After the build completes, tag your image so you can push the image to this repository:<br>
```docker tag chair:latest 012672079470.dkr.ecr.us-west-1.amazonaws.com/chair:latest```

4. Run the following command to push this image to your newly created AWS repository:<br>
```docker push 012672079470.dkr.ecr.us-west-1.amazonaws.com/chair:latest```


## Required Environment
Retrieve these secrets from the twillio environment (Environment Settings)

| Environment Variable | Description                         | Required              | Default |
| -------------------- | ----------------------------------- | --------------------- | ------- |
| LOG_LOCAL            | Log to local STDOUT                 | No                    | False   |
| INTERVAL_SEC         | Period of time to wait for re-run   | No                    | 60      |
| ACCOUNT_SID          | The account identifier of the owner | Yes                   | None    |
| AUTH_TOKEN           | Authentication token from twilio    | Yes                   | None    |
| SENDER_PHONE         | Sender's phone number               | Yes                   | None    |
| RECEIVER_PHONE       | Target recipient's phone number     | Yes                   | None    |
| URL_REG              | URL of registration phone message   | Yes                   | None    |
| URL_TEST             | URL of test phone message           | Yes                   | None    |
| URL_WARNING          | URL of warning phone message        | Yes                   | None    |
| LOG_GROUP_NAME       | Specify your log group name here    | If LOG_LOCAL Disabled | None    |


# Twilio Context
Recommend setting up twilio with recurring billing in case it runs out

## String Identifier SID
SID stands for String Identifier. It's a unique key that is used to identify specific resources. At Twilio, each SID has 34 digits and you can identify the type of SID and the product it's associated with by the first two characters. Your Twilio SID can be retrieved from the console located at https://console.twilio.com/.

## Authentication Token
Twilio uses two credentials to determine which account an API request is coming from: The Account SID, which acts as a username, and the Auth Token which acts as a password. This guide explains how to find your Auth Token, and how to change it.

## Sender and Reciever Phone Numbers
Twilio uses two phone numbers to execute sms messages and calls. The FROM phone number is going to be from the device you setup in Twilio. This is a critical step and can be accomplished from the console. If you dont have the correct FROM number the messages and calls will not succeed. The TO number is your phone that you want to be notified on.
# Chair
Chair is a python both that makes requests to the blackhat training page and when the page 200's it notifies the target phone number via sms and phone call. The image will send an initial test message and perform a test call when you set it up. If it doesn't do this something is probably wrong.

# Contributors
## Nate Singer
#### nathaniel\<at\>singer\<dot\>cloud
I wrote this bot to take a shot at a Blackhat AWE seat for the 2023 offering. Results to be determined but you are welcome to take advantage of this tool or fork/pull additional features as you'd like.

# Artifact Build & Execution
## GAR Authentication and Build Process
1. Authenticate to docker<br>
```gcloud auth login```

2. Configure auth for docker (config file)<br>
```gcloud auth configure-docker us-central1-docker.pkg.dev```

3. Verify authentication by pulling your secret<br>
```echo "https://us-central1-docker.pkg.dev" | docker-credential-gcr get```

## Image Assembly & Push
1. Build the image locally<br>
```docker build . -t chair```

2. Tag the local image<br>
```docker tag chair us-central1-docker.pkg.dev/<project>/<repository>/chair:<version>```

3. Push it to the artifacts repository<br>
```docker push chair us-central1-docker.pkg.dev/<project>/<repository>/chair:<version>```

## Required Environment
Retrieve these secrets from the twillio environment (Environment Settings)

| Environment Variable | Description                         | Required | Default |
| -------------------- | ----------------------------------- | -------- | ------- |
| LOG_LOCAL            | Log to local STDOUT                 | No       | False   |
| INTERVAL_SEC         | Period of time to wait for re-run   | No       | 60      |
| ACCOUNT_SID          | The account identifier of the owner | Yes      | None    |
| AUTH_TOKEN           | Authentication token from twilio    | Yes      | None    |
| SENDER_PHONE         | Sender's phone number               | Yes      | None    |
| RECEIVER_PHONE       | Target recipient's phone number     | Yes      | None    |
| URL_REG              | URL of registration phone message   | Yes      | None    |
| URL_TEST             | URL of test phone message           | Yes      | None    |
| URL_WARNING          | URL of warning phone message        | Yes      | None    |


# Twilio Context
Recommend setting up twilio with recurring billing in case it runs out

## String Identifier SID
SID stands for String Identifier. It's a unique key that is used to identify specific resources. At Twilio, each SID has 34 digits and you can identify the type of SID and the product it's associated with by the first two characters. Your Twilio SID can be retrieved from the console located at https://console.twilio.com/.

## Authentication Token
Twilio uses two credentials to determine which account an API request is coming from: The Account SID, which acts as a username, and the Auth Token which acts as a password. This guide explains how to find your Auth Token, and how to change it.

## Sender and Reciever Phone Numbers
Twilio uses two phone numbers to execute sms messages and calls. The FROM phone number is going to be from the device you setup in Twilio. This is a critical step and can be accomplished from the console. If you dont have the correct FROM number the messages and calls will not succeed. The TO number is your phone that you want to be notified on.
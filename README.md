# Sms service

This service has been created using Python 3.7 and Twilio platform to enable you to engage customers across the channel SMS.
The application was deployed in Heroku and actually is used in a large number of service cells of eva conversational flows.

## Prerequisites

- 	Python 3.7+
- 	Postman
- 	Cloud account (Azure, GCP, Heroku, etc)

## Local testing
-  Run the file app.py 
-  Send this cURL with your fauvorite rest service client (I prefer Postman)

```json
curl --location --request POST '[URL]' \
--header 'Content-Type: application/json' \
--data-raw '{
    "asunto":"[ASUNTO]",
    "body":"[BODY]",
    "numero":"[NUMERO]"
}'
```

Where:
- 	[URL]: Refers to the service endpoint
- 	[ASUNTO]: Refers to the subject of the message
- 	[BODY]: Refers to the content of the message
- 	[NUMERO]: Refers to the destination number

Considerations when deploying GCP
- 	To the main file you have to put main
- 	You have to indicate the first function that should run
- 	This function must be passed as a parameter self
- 	You have to extend the app's permissions

Permission extension
- 	Go to the Google Cloud Console
- 	Click the checkbox next to the role you want to grant access to.
- 	Click Show dashboard in the upper right corner to bring up the Permissions tab
- 	Click Add Member
- 	In the New Members field, type allUsers
- 	Select the Cloud Functions function> Cloud Functions Invoker from the Select a function drop-down menu
- 	Click Save



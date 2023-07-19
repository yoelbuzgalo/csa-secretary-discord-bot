This is a discord server bot that I made, it takes in the user input and forwards the data to a google sheet for convenience of patrol log submission within the server.

To use this bot, you will need to do the following:

1. create a file in the root directory named "history.json" and add inside:

{ "patrol_id": 0 }

2. Create a google service account for your google sheet and add it to the root directory and name it:

service_account_credentials.json

For more information, read here: https://docs.gspread.org/en/v5.10.0/oauth2.html#enable-api-access

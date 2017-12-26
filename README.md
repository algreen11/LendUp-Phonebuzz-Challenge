# Phone Buzz ! 

## Getting Started

1. ```pip install -r requirements.txt```

2. For phase1 : Clone repo, download and unzip ngrok 

3. Insert your twilio account details at the top of app.py
``` 
account_sid = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twilio_phone_number = '+11234567890'
```

## Run phase 1 - simple Twiml Phonebuzz

1. Navigate to the cloned repo and run ```python3 app.py```

2. In a different terminal window run ```./ngrok 5000```

3. In your twilio dashboard change ```'A call comes in'``` to the ngrok web address plus ```/phase1```, for example ```https://7e76d634.ngrok.io/phase1```

4. Now to play just call your twilio number!


## Run phase 2 - A very simple dialing phonebuzz
1. Simply visit [https://alexphonebuzz.herokuapp.com/](https://alexphonebuzz.herokuapp.com/) or run ```python3 app.py``` locally

2. Enter in your phone number to play! 

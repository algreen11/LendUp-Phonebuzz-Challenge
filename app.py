from flask import Flask, request, abort, render_template, redirect, url_for
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Gather, Say
from twilio.request_validator import RequestValidator


app = Flask(__name__)

account_sid = "TWILIO ACCOUNT SID"
auth_token = "TWILIO ACCOUNT AUTH TOKEN"
twilio_phone_number = 'TWILIO NUMBER'


def fizz_buzz(val):
    output = []
    for i in range(1, val+1):
        if i % 3 == 0 and i % 5 == 0:
            output.append("Fizz Buzz.")  # periods make it so that voice is understandable
        elif i % 5 == 0:
            output.append("Buzz.")
        elif i % 3 == 0:
            output.append("Fizz.")
        else:
            output.append(str(i) + ".")
    return output


def validate_twilio_request():
    validator = RequestValidator(auth_token)
    url = request.url[:4] + 's' + request.url[4:]  # add s because request comes in without it
    request_valid = validator.validate(
            url,
            request.form,
            request.headers.get('X-TWILIO-SIGNATURE', ''))
    if not request_valid:
        return abort(403)


def gather_input():
    response = VoiceResponse()
    gather = Gather(num_digits=2, action='/handle_input', method="POST")
    gather.say("Please enter a two digit number to play fizz buzz.")
    response.append(gather)
    response.say("You didnt input anything, bye bye.")  # if timeout on entry

    return str(response)


@app.route("/phase1", methods=['GET', 'POST'])
def open():
    validate_twilio_request()
    return gather_input()


@app.route("/handle_input", methods=['GET', 'POST'])
def user_input():
    num = request.values.get('Digits', None)
    response = VoiceResponse()

    if num.isdigit():  # checks to make sure user entered a number
        output = fizz_buzz(int(num))
        response.say(" ".join(output))
        return str(response)
    else:
        response.say("The input wasn't digits. Feel free to try again")
        return str(response)


@app.route("/")
def outbound():
    return render_template("index.html")


@app.route("/", methods=['POST'])
def dial_number():
    number = request.form['number']
    if len(number) != 12 or number[0] != '+' or not number[1:].isdigit():
        return redirect('/')
    client = Client(account_sid, auth_token)
    call = client.calls.create(to=number, from_=twilio_phone_number, url='https://alexphonebuzz.herokuapp.com/phase2')
    return redirect('/')


@app.route("/phase2", methods=['GET', 'POST'])
def calling():
    return gather_input()


if __name__ == "__main__":
    app.run(debug=True)

import os
from flask import Flask, request, Response
import config
from slackclient



app = Flask(__name__)

SLACK_WEBHOOK_SECRET = config.SLACK_TOKEN
sc = SlackClient(SLACK_WEBHOOK_SECRET)


@app.route('/', methods=['GET'])
def test():
    return "hello"





if __name__ == "__main__":
    app.run(debug=True)

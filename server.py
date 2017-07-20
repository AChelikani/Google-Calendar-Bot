import os
from flask import Flask, request, Response
import config
from slackclient import SlackClient



app = Flask(__name__)

SLACK_WEBHOOK_SECRET = config.SLACK_TOKEN
sc = SlackClient(SLACK_WEBHOOK_SECRET)


@app.route('/', methods=['GET'])
def test():
    return "hello"

@app.route("/event-action", methods=['GET', 'POST'])
def action():
	params = request.get_json()
	if params['type'] == 'url_verification':
		token, ch = params['token'], params['challenge']
		return ch, {'Content-Type': 'text/plain'}
	else:
		url = 'https://dev.slack.com/api/chat.unfurl'
		token = 'xoxp-11806974912-11806974928-11814168160-274b45cf1397a0dfbedc91a6653a3fe4'
		ts = params['event']['message_ts']
		unfurl_url = params['event']['links'][0]['url']
		channel = params['event']['channel']
		unfurls = {
							  unfurl_url: {
							    "title": "Let's pretend we're on a rocket ship to Neptune",
							    "text": "The planet Neptune looms near. What do you want to do?",
							    "callback_id": "imagine_001",
							    "attachment_type": "default",
							    "fallback": "Pretend your rocket ship is approaching Neptune. What do you want to do next?",
							    "actions": [
							      {
							        "name": "decision",
							        "value": "orbit",
							        "style": "primary",
							        "text": "Orbit",
							        "type": "button"
							      },
							      {
							        "name": "decision",
							        "value": "land",
							        "text": "Attempt to land",
							        "type": "button"
							      },
							      {
							        "name": "decision",
							        "value": "self_destruct",
							        "text": "Self destruct",
							        "type": "button",
							        "style": "danger",
							      }
							    ]
							  }
							}
		payload = {'token': token, 'channel': channel, 'ts': ts, 'unfurls': json.dumps(unfurls)}
		print 'doing unfurl for', unfurl_url
		r = requests.post(url, data=payload)
		return str(r.status_code)



if __name__ == "__main__":
    app.run(debug=True)

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
	print 'hi advith ty 4 reacting'
	params = request.get_json()
	print params
	if params['type'] == 'url_verification':
		token, ch = params['token'], params['challenge']
		return ch, {'Content-Type': 'text/plain'}
	else:
		# payload = {'token': token, 'channel': channel, 'ts': ts, 'unfurls': json.dumps(unfurls)}
		# r = requests.post(url, data=payload);
		user = params['event']['user']
		event_type = params['event']['user']
		item = params['event']['item']
		print 'what is this item?', item
		return '200'



if __name__ == "__main__":
    app.run(debug=True)

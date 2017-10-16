from flask import Flask 
import requests, json

app = Flask(__name__)


@app.route('/hi', methods=['GET'])
def hi():
    return "hi"

@app.route('/', methods=['POST'])
def handle_message():
    # return "hi!"
    from IPython import embed; embed()
    url = 'https://hooks.slack.com/services/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',
    payload = {'text': 'hellow world!!!!! from python'},
    r = requests.post(url, json=payload)
# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' 
# https://hooks.slack.com/services/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
    from IPython import embed; embed()
    return r

if __name__ == '__main__':
    print ("Server running on port 8000")
    app.run(port=8000)

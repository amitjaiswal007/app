from flask import Flask, request, jsonify, make_response	
import textblob as tb
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
	text = request.args.get('text')
	analysis = tb.TextBlob( text)
	sentiment = analysis.sentiment
	data = {'sentiment':sentiment[0]}
	r = make_response( jsonify( data), 20)
	return r
	

if __name__ == '__main__':
	app.run()
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_string():
	data = request.json
	print(f"input: {data}")
	if 'string' not in data:
		return jsonify({"error": "No string provided"}), 400
	
	response = requests.post('http://processor:5001/process', json={"string": data['string']})
	return jsonify(response.json())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

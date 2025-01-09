from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def send_string():
	data = request.json
	if 'string' not in data:
		return jsonify({"error": "No string provided"}), 400
	
	response = requests.post('http://processor:5001/process', json={"string": data['string']})
	print(f"Sent data: {data}, Response: {response.json()}")
	return jsonify({"input": f"Sent data: {data}"} | response.json())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)

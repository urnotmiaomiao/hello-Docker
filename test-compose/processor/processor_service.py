from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process_string():
	data = request.json
	print(f"processor: {data}")
	if 'string' not in data:
		return jsonify({"error": "No string provided"}), 400
		
	transformed_string = data['string'][::-1]
	transformed_data = {"transformed": transformed_string}
	response = requests.post('http://output:5002/store', json=transformed_data)
	print(f"Sent data: {transformed_data}, Response: {response.json()}")
	return jsonify({"Processor": f"Processed data: {transformed_data}"} | response.json())
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5001)

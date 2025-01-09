from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/store', methods=["POST"])
def store_string():
	data = request.json
	print(f"output: {data}")
	if 'transformed' not in data:
		return jsonify({"error": "No transformed string provided"}), 400
	
	with open('/app/output_data/output.txt', 'w') as f:
		f.write(data['transformed'])
	
	return jsonify({"message": "String stored successfully!"})
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port =5002)

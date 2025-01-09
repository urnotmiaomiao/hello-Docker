import time
import requests

INPUT_SERVICE_URL = "http://input:5000/send"

def generate_data():
	return f"Generated String at {time.ctime()}"

def send_data(): 
	while True:
		data = {"string": generate_data()}
		try:
			response = requests.post(INPUT_SERVICE_URL, json=data)
			print(f"Sent data: {data}, Response: {response.json()}")
		except requests.exceptions.RequestException as e:
			print(f"Error sending data: {e}") 
		time.sleep(5)
		
if __name__ == "__main__":
	send_data()

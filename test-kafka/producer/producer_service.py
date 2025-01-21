from kafka import KafkaProducer
import time

KAFKA_BROKER = "kafka:9092"
TOPIC = "input_topic"

# producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)

while True:
	try: 
		producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
		print("== Producer connected to Kafka! ==")
		break
	except Exception as e:
		print(f"== Producer: Kafka not ready. Retrying in 5 seconds... Error: {e} ==")
		time.sleep(5)


def generate_data():
	return f"Generated String at {time.ctime()}"

def send_data(): 
	while True:
		msg = generate_data()
		producer.send(TOPIC, value=msg.encode('utf-8'))
		print(f"Sent: {generate_data()}")
		time.sleep(5)
		
if __name__ == "__main__":
	send_data()

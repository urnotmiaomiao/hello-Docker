from kafka import KafkaConsumer
import time
from pathlib import Path

KAFKA_BROKER = "kafka:9092"
CONSUME_TOPIC = "output_topic"
OUTPUT_FILE = Path("/app/output_data/processed_strings.txt")

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)


while True:
	try:
		consumer = KafkaConsumer(CONSUME_TOPIC, bootstrap_servers=KAFKA_BROKER)
		print("== Output connected to Kafka! ==")
		break
	except Exception as e:
		print(f"== Output: Kafka not ready. Retrying in 5 seconds... Error: {e} ==")
		time.sleep(5)
# consumer = KafkaConsumer(CONSUME_TOPIC, bootstrap_servers=KAFKA_BROKER)

def store_string():
	with open(OUTPUT_FILE, "a") as f:
		for message in consumer:
			data = message.value.decode('utf-8')
			print(f"Output service received: {data}")
			f.write(data + "\n")
			f.flush() 
	
if __name__ == "__main__":
	store_string()

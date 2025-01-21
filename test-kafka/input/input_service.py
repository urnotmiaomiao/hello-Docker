import time
from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER = "kafka:9092"
CONSUME_TOPIC = "input_topic"
PRODUCE_TOPIC = "processor_topic"

while True:
	try:
		consumer = KafkaConsumer(CONSUME_TOPIC, bootstrap_servers=KAFKA_BROKER)
		producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
		print("== Input connected to Kafka! ==")
		break
	except Exception as e:
		print(f"== Input: Kafka not ready. Retrying in 5 seconds... Error: {e} ==")
		time.sleep(5)

def send_string():
	for message in consumer:
		data = message.value.decode('utf-8')
		print(f"Input service received: {data}")
		producer.send(PRODUCE_TOPIC, value=data.encode('utf-8'))
		print(f"Forwarded to Processor: {data}")
	
if __name__ == "__main__":
	send_string()

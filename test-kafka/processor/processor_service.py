import time
from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER = "kafka:9092"
CONSUME_TOPIC = "processor_topic"
PRODUCE_TOPIC = "output_topic"


while True:
	try:
		consumer = KafkaConsumer(CONSUME_TOPIC, bootstrap_servers=KAFKA_BROKER)
		producer = KafkaProducer(bootstrap_servers=KAFKA_BROKER)
		print("== Processor connected to Kafka! ==")
		break
	except Exception as e:
		print(f"== Processor: Kafka not ready. Retrying in 5 seconds... Error: {e} ==")
		time.sleep(5)


def process_string():
	for message in consumer:
		data = message.value.decode('utf-8')
		print(f"Processor received: {data}")
		processed_data = data[::-1]
		producer.send(PRODUCE_TOPIC, value=processed_data.encode('utf-8'))
		print(f"Processed & sent: {processed_data}") 
	
if __name__ == "__main__":
	process_string()

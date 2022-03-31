from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='192.168.1.12:9092')

while True:
    topic = input("topic\n")
    message = input("enter input\n")
    producer.send(topic, str.encode(message))

from mqttasgi.consumers import MqttConsumer
class MyMqttConsumer(MqttConsumer):

    async def connect(self):
        await self.subscribe('test', 2)

    async def receive(self, mqtt_message):
        print('Received a message at topic:', mqtt_message['topic'])
        print('With payload', mqtt_message['payload'])
        print('And QOS:', mqtt_message['qos'])
        pass

    async def disconnect(self):
        await self.unsubscribe('test')
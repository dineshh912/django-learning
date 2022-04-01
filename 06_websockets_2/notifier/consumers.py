from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer
import asyncio


class EchoConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        # Echo the same received payload
        await self.send({
            "type": "websocket.send",
            "text": event["text"]
        })


class TickTockConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        await self.accept()

        while 1:
            await asyncio.sleep(1)
            await self.send_json("Tick")
            await asyncio.sleep(1)
            await self.send_json("Tock")


class UserCreatedConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):

        await self.accept()
        await self.channel_layer.group_add("gossip", self.channel_name)
        print(f"added {self.channel_name} Channel to gossip")

    
    async def disconnect(self, close_code):

        await self.channel_layer.group_discard("gossip", self.channel_name)
        print(f"Removed {self.channel_name} Channel to gossip")

    
    async def websocket_receive(self, event):
        # Echo the same received payload
        print(event)
    
    
    async def user_gossip(self, event):

        await self.send_json(event)
        print(f"got message {event} at {self.channel_name}")
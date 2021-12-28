import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import ChatUser,Message
from CustomUserModel.models import CustomUser


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("i am in cosumenr")
        self.other_user = self.scope['url_route']['kwargs']['user_name']
        self.me = self.scope['user']
        print('userssssssssssssssssssssss',self.other_user,self.me)
        my_chat_room = await self.person_obj_id(me=self.me,other=self.other_user)
        room_name = my_chat_room
        self.room_group_name = 'chat_%s'% room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()

    @database_sync_to_async
    def person_obj_id(self, me, other):
        p = ChatUser.objects.get_or_new(me, other)
        print('chat usersssssss',p)
        return p[0]

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        print(message,"i am in message")
        uname = data['uname']
        # image = data['image']
        self.create_chat_message = await self.create_my_message(uname=self.me, message=message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message or None,
                # 'image':image or None,
                'uname':uname,
            }
        )

    # Receive message from room group
    async def chat_message(self,event):
        message = event['message']
        uname = event['uname']
        # image = event['image']

        await self.send(text_data=json.dumps({
            'message':message or None,
            # 'image': image or None,
            'uname' : uname,
        }))
    @database_sync_to_async
    def create_my_message(self,uname,message):
        o1 = CustomUser.objects.get(username=self.me)
        o2 = CustomUser.objects.get(username=self.other_user)
        my_msg = ChatUser.objects.get_or_new(me=o1,other=o2)[0]
        e = Message.objects.create(user=uname, message=message, person=my_msg)
        return print('msg created',e)

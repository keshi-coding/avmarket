from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.utils import timezone
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user1 = self.scope['user']
        self.user2 = self.scope['url_route']['kwargs']['user2']

        self.room_name = f"{min(self.user1.username, self.user2)}_{max(self.user1.username, self.user2)}"
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"✅ WebSocket conectado para {self.user1.username} e {self.user2}")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json.get('message', '')

        remetente = self.scope['user']
        destinatario_username = self.user2

        destinatario = await self.get_user(destinatario_username)  # ✅ Assíncrono

        if destinatario:
            await self.salvar_mensagem(remetente, destinatario, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user1": remetente.username,
                "user2": destinatario.username
            }
        )

    async def chat_message(self, event):
        message = event["message"]
        user1 = event["user1"]
        user2 = event["user2"]

        print(f"📩 Mensagem recebida no backend: {user1} -> {user2}: {message}")

        await self.send(text_data=json.dumps({
            "message": message,
            "user1": user1,
            "user2": user2
        }))

    async def disconnect(self, close_code):
        print(f"🔴 WebSocket fechado! Código: {close_code}")

    @sync_to_async
    def get_user(self, username):
        from django.contrib.auth.models import User
        """Busca um usuário no banco de dados de forma assíncrona"""
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @sync_to_async
    def salvar_mensagem(self, remetente, destinatario, message):
        from av_app.models import Mensagem
        """Salva a mensagem e atualiza o ChatRecentes no banco de forma assíncrona"""
        Mensagem.objects.create(
            remetente=remetente,
            destinatario=destinatario,
            conteudo=message,
            timestamp=timezone.now(),
        )

        from av_app.models import ChatRecentes
        ChatRecentes.objects.update_or_create(
            usuario=remetente,
            contato=destinatario,
            defaults={'ultima_mensagem': timezone.now()}
        )

        ChatRecentes.objects.update_or_create(
            usuario=destinatario,
            contato=remetente,
            defaults={'ultima_mensagem': timezone.now()}
        )

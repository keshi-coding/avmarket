import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from django.urls import path  # <- Adicione esta linha
from av_app import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'av_project.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<str:user1>/<str:user2>/', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})

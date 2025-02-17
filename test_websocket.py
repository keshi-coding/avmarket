import asyncio
from channels.testing import WebsocketCommunicator
from av_project.asgi import application
import json

# Função para testar a comunicação WebSocket
async def test_websocket():
    room_name = "keshicoding"
    communicator = WebsocketCommunicator(application, f"/ws/chat/{room_name}/")
    connected, subprotocol = await communicator.connect()

    print(f"Conectado: {connected}")
    print(f"Subprotocolo: {subprotocol}")

    # Enviar uma mensagem de teste
    message = "Olá, mundo!"
    await communicator.send_json_to({
        'message': message
    })

    # Esperar pela resposta
    response = await communicator.receive_json_from()
    print(f"Mensagem recebida: {response['message']}")

    # Fechar a conexão
    await communicator.disconnect()

# Executar a função
asyncio.run(test_websocket())

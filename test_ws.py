import asyncio
from channels.layers import get_channel_layer

async def test_ws():
    channel_layer = get_channel_layer()
    try:
        await channel_layer.send('test_channel', {'type': 'test.message', 'message': 'Hello'})
        print('WebSocket está funcionando!')
    except Exception as e:
        print('Erro no WebSocket:', e)

asyncio.run(test_ws())

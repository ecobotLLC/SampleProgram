import asyncio
import websockets

async def websocket_client():
	uri = "ws://localhost:8080"  # WebSocketサーバーのアドレスに合わせて変更してください

	async with websockets.connect(uri) as websocket:
		while True:
			# 接続が確立された後の処理
			message = input("メッセージを入力してください: ")
			await websocket.send(message)
			
			response = await websocket.recv()
			print(f"サーバーからの応答: {response}")

asyncio.get_event_loop().run_until_complete(websocket_client())

import asyncio
import websockets
import hashlib
from datetime import datetime

def calculate_sha256(input_string):
    # 文字列をUTF-8エンコーディングでバイト列に変換
    byte_string = input_string.encode('utf-8')

    # SHA-256ハッシュオブジェクトを作成
    sha256_hash = hashlib.sha256()

    # バイト列をハッシュに追加
    sha256_hash.update(byte_string)

    # ハッシュを16進数文字列として取得
    hashed_string = sha256_hash.hexdigest()

    return hashed_string
async def websocket_client():
	uri = "ws://localhost:8080"  # WebSocketサーバーのアドレスに合わせて変更してください
	# JSONファイルのパス
	json_file_path = 'sample_insert_reservation_data.json'
	# json_file_path = 'sample_update_cleaner_reservation_data.json'
	# JSONファイルの読み込み
	with open(json_file_path, 'r') as text_file:
		file_content = text_file.read()
	async with websockets.connect(uri) as websocket:
		while True:
			# 接続が確立された後の処理
			# message_tmp = input("メッセージを入力してください: ")
			message = file_content
			hashed_result = calculate_sha256(message)
			# print(f"hashcode:{hashed_result}")
			# print(f"sendmesage:{hashed_result + message}")
			await websocket.send(hashed_result + message)
			
			response = await websocket.recv()
			current_time = datetime.now()

			# ミリ秒までのフォーマット
			formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

			print(f"サーバーからの応答{formatted_time}: {response}")

asyncio.get_event_loop().run_until_complete(websocket_client())

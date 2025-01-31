# import aiohttp
# import asyncio

# async def fetch_user_data(user_id: int):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(f"https://enka.network/api/uid/{user_id}?info") as response:
#             if response.status != 200: return None, None, None

#             data = await response.json()

#             player_info = data["playerInfo"]
#             user_name = player_info["nickname"]   # ユーザー名
#             adventure_rank = player_info["level"]   # 冒険ランク
#             status_msg = player_info["signature"]   # ステータスメッセージ

#             return user_name, adventure_rank, status_msg

# async def main():
#     user_id = 819312869
#     nickname, level, signature = await fetch_user_data(user_id)
#     print(f"{nickname} Lv.{level} {signature}")

# if __name__ == "__main__":
#     asyncio.run(main())

import requests

def fetch_user_data(user_id: int):
    response = requests.get(f"https://enka.network/api/uid/{user_id}?info")
    if response.status_code != 200: return None, None, None

    data = response.json()

    player_info = data["playerInfo"]
    user_name = player_info["nickname"]   # ユーザー名
    adventure_rank = player_info["level"]   # 冒険ランク
    status_msg = player_info["signature"]   # ステータスメッセージ

    return user_name, adventure_rank, status_msg

if __name__ == "__main__":
    user_id = 819312869
    nickname, level, signature = fetch_user_data(user_id)
    print(f"{nickname} Lv.{level} {signature}")
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
import json

def fetch_user_data(user_id: int):
    response = requests.get(f"https://enka.network/api/uid/{user_id}?info")

    if response.status_code != 200: return None

    try:
        data = response.json()
        # print(json.dumps(data, indent=2))
        return {
            "user_name": data["playerInfo"]["nickname"],  # ユーザー名
            "adventure_rank": data["playerInfo"]["level"],  # 冒険ランク
            "status_msg": data["playerInfo"]["signature"],  # ステータスメッセージ
            "achievement": data["playerInfo"]["achievement"],  # アチーブメント数
            "tower": {
                "floor": data["playerInfo"]["towerFloorIndex"],  # 螺旋層
                "level": data["playerInfo"]["towerLevelIndex"],  # 螺旋階
                "star": data["playerInfo"]["towerStarIndex"]  # 螺旋星
            },
            "theater": {
                "act": data["playerInfo"]["theaterActIndex"],  # 劇場幕
                "mode": data["playerInfo"]["theaterModeIndex"],  # 劇場モード
                "star": data["playerInfo"]["theaterStarIndex"]  # 劇場星
            }
        }
    except KeyError:
        return None

if __name__ == "__main__":
    user_id = 819312869
    if user_info := fetch_user_data(user_id):
        nickname = user_info["user_name"]
        level = user_info["adventure_rank"]
        signature = user_info["status_msg"]
        tower_floor = user_info["tower"]["floor"]
        tower_level = user_info["tower"]["level"]
        theater_act = user_info["theater"]["act"]
        theater_mode = user_info["theater"]["mode"]
        theater_star = user_info["theater"]["star"]
        print(f"{nickname} Lv.{level} {signature} {tower_floor} {tower_level} {theater_act} {theater_mode} {theater_star}")
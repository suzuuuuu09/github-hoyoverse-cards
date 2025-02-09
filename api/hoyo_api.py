import aiohttp
import asyncio
import json

async def fetch_user_data(user_id: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://enka.network/api/uid/{user_id}?info") as response:
            if response.status != 200:
                return None

            try:
                data = await response.json()

                player_info = data["playerInfo"]
                base_user_info = {
                    "user_name": player_info["nickname"],  # ユーザー名
                    "adventure_rank": player_info["level"],  # 冒険ランク
                    "status_msg": player_info.get("signature"),  # ステータスメッセージ
                    "achievement": player_info.get("finishAchievementNum"),  # アチーブメント数
                    "friendship_max": player_info.get("fetterCount")  # 好感度MAXキャラ数
                }

                # 螺旋
                tower_info = {
                    "floor": player_info.get("towerFloorIndex"),  # 螺旋層
                    "level": player_info.get("towerLevelIndex"),  # 螺旋間
                    "star": player_info.get("towerStarIndex")  # 螺旋星
                }
                base_user_info["tower"] = tower_info

                # 幻想シアター
                theater_info = {
                    "act": player_info.get("theaterActIndex"),  # 幻想シアター幕
                    "mode": player_info.get("theaterModeIndex"),  # 幻想シアターモード
                    "star": player_info.get("theaterStarIndex")  # 幻想シアター星
                }
                base_user_info["theater"] = theater_info

                return base_user_info
            except KeyError:
                return None

if __name__ == "__main__":
    user_id = 801081402

    user_info = asyncio.run(fetch_user_data(user_id))
    print(user_info)
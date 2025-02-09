from dataclasses import dataclass
import aiohttp
import asyncio
from typing import Optional, Dict, Any

@dataclass
class TowerInfo:
    """深境螺旋の情報を格納するデータクラス"""
    floor: Optional[int] = None  # 螺旋層
    level: Optional[int] = None  # 螺旋間
    star: Optional[int] = None   # 螺旋星

@dataclass
class TheaterInfo:
    """幻想シアターの情報を格納するデータクラス"""
    act: Optional[int] = None    # 幻想シアター幕
    mode: Optional[int] = None   # 幻想シアターモード
    star: Optional[int] = None   # 幻想シアター星

@dataclass
class UserInfo:
    """ユーザー情報を格納するデータクラス"""
    user_name: str                      # ユーザー名
    adventure_rank: int                 # 冒険ランク
    status_msg: Optional[str] = None    # ステータスメッセージ
    achievement: Optional[int] = None   # アチーブメント数
    friendship_max: Optional[int] = None # 好感度MAXキャラ数
    tower: Optional[TowerInfo] = None   # 螺旋情報
    theater: Optional[TheaterInfo] = None # 幻想シアター情報

class EnkaNetworkAPI:
    """EnkaNetworkのAPIを扱うクラス"""
    BASE_URL = "https://enka.network/api/uid"

    @staticmethod
    async def fetch_user_data(user_id: int) -> Optional[UserInfo]:
        """ユーザー情報を取得する"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"{EnkaNetworkAPI.BASE_URL}/{user_id}?info") as response:
                    if response.status != 200:
                        return None

                    data = await response.json()
                    return EnkaNetworkAPI._parse_user_data(data)
        except (aiohttp.ClientError, asyncio.TimeoutError):
            return None

    @staticmethod
    def _parse_user_data(data: Dict[str, Any]) -> Optional[UserInfo]:
        """APIレスポンスからユーザー情報を解析する"""
        try:
            player_info = data["playerInfo"]

            tower_info = TowerInfo(
                floor=player_info.get("towerFloorIndex"),
                level=player_info.get("towerLevelIndex"),
                star=player_info.get("towerStarIndex")
            )

            theater_info = TheaterInfo(
                act=player_info.get("theaterActIndex"),
                mode=player_info.get("theaterModeIndex"),
                star=player_info.get("theaterStarIndex")
            )
            
            return UserInfo(
                user_name=player_info["nickname"],
                adventure_rank=player_info["level"],
                status_msg=player_info.get("signature"),
                achievement=player_info.get("finishAchievementNum"),
                friendship_max=player_info.get("fetterCount"),
                tower=tower_info,
                theater=theater_info
            )
        except KeyError:
            return None

async def fetch_user_data(user_id: int) -> Optional[UserInfo]:
    """ユーザー情報を取得する（後方互換性のための関数）"""
    return await EnkaNetworkAPI.fetch_user_data(user_id)

if __name__ == "__main__":
    user_id = 801081402
    user_info = asyncio.run(fetch_user_data(user_id))

    if user_info:
        print(f"ユーザー名: {user_info.user_name}")
        print(f"冒険ランク: {user_info.adventure_rank}")
        if user_info.tower:
            print(f"螺旋: {user_info.tower.floor}-{user_info.tower.level}")
        if user_info.theater:
            print(f"幻想シアター: 第{user_info.theater.act}幕")
    else:
        print("ユーザー情報の取得に失敗しました")
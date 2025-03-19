import requests
import json
from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class GenshinImpactUserInfo:
    """原神のユーザー情報を格納するデータクラス"""
    user_name: str              # ユーザー名
    adventure_rank: int         # 冒険ランク
    active_days: int            # アクティブ日数
    achievement: int            # アチーブメント数
    tower: str                  # 深境螺旋
    theater: int                # 幻想シアター
    full_fetter_avatar: int         # 好感度MAXキャラ数
    characters: int             # キャラクター数
    

def genshin_user_info(uid: int):
    """ユーザー情報を取得する"""
    url = "https://bbs-api-os.hoyoverse.com/game_record/genshin/api/index"

    params = {
        "role_id": uid,
        "server": "os_asia",
        "schedule_type": 1,
    }

    ltoken = getenv("HOYOLAB_LTOKEN")
    ltuid = getenv("HOYOLAB_LTUID")

    headers = {
        "Cookie": f"ltoken_v2={ltoken}; ltuid_v2={ltuid};",
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data']
        else:
            return None
    else:
        return None
if __name__ == "__main__":
    load_dotenv()
    uid = 801870399
    data = genshin_user_info(uid)
    
    gi_user_info = GenshinImpactUserInfo(
        user_name = data['role']['nickname'],
        adventure_rank = data['role']['level'],
        active_days = data['stats']['active_day_number'],
        achievement = data['stats']['achievement_number'],
        tower = data['stats']['spiral_abyss'],
        theater = data['stats']['role_combat']['max_round_id'],
        full_fetter_avatar = data['stats']['full_fetter_avatar_num'],
        characters = data['stats']['avatar_number'],
    )

    print(gi_user_info)
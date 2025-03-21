import requests
import json
from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass
from utils import generate_ds

@dataclass
class GenshinImpactUserInfo:
    """原神のユーザー情報を格納するデータクラス"""
    user_name: str              # ユーザー名
    adventure_rank: int         # 冒険ランク
    active_days: int            # アクティブ日数
    achievement: int            # アチーブメント数
    tower: str                  # 深境螺旋
    theater: int                # 幻想シアター
    full_fetter_avatar: int     # 好感度MAXキャラ数
    characters: int             # キャラクター獲得数

@dataclass
class HonkaiStarRailUserInfo:
    """崩壊スターレイルのユーザー情報を格納するデータクラス"""
    user_name: str              # ユーザー名
    active_days: int            # アクティブ日数
    achievement: int            # アチーブメント
    characters: int             # キャラクター獲得数
    trailblaze_level: int       # 開拓者レベル
    frogotten_hall: int         # 忘却の庭
    pure_fiction: int           # 虚構叙事
    apocalyptic_shadow: int     # 末日の幻影

@dataclass
class ZenlessZoneZeroUserInfo:
    """ゼンレスゾーンゼロのユーザー情報を格納するデータクラス"""
    user_name: str              # ユーザー名
    interknot_level: int        # インターノットレベル
    active_days: int            # アクティブ日数
    achievement: int            # アチーブメント数
    agents: int                 # エージェント獲得数
    bangboo: int                # ポンプ獲得数
    deadly_assault: int         # 危局強襲戦
    shiyu_defense_frontier: int # 式輿防衛戦
    hollow_zero_level: int      # 零号ホロウ

BBS_API = "https://bbs-api-os.hoyolab.com"

def genshin_user_info(uid: int):
    """ユーザー情報を取得する"""
    GENSHIN_INDEX_URL = f"{BBS_API}/game_record/genshin/api/index"

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

    response = requests.get(GENSHIN_INDEX_URL, params=params, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['data']:
            return data['data']
        else:
            return None
    else:
        return None
    
def honkai_star_rail_user_info(uid: int):
    """ユーザー情報を取得する"""
    HSR_INDEX_URL = f"{BBS_API}/game_record/hkrpg/api/index"
    params = {
        "role_id": uid,
        "server": "prod_official_asia",
    }

    ltoken = getenv("HOYOLAB_LTOKEN")
    ltuid = getenv("HOYOLAB_LTUID")
    ds = generate_ds()

    headers = {
        "Cookie": f"ltoken_v2={ltoken}; ltuid_v2={ltuid};",
        "DS": ds,
        "x-rpc-app_version": "2.67.1",
        "x-rpc-client_type": "5",
        "x-rpc-language": "ja-jp"
    }

    response = requests.get(HSR_INDEX_URL, params=params, headers=headers)
    
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
    gi_uid = 801870399
    gi_data = genshin_user_info(gi_uid)
    
    gi_user_info = GenshinImpactUserInfo(
        user_name = gi_data['role']['nickname'],
        adventure_rank = gi_data['role']['level'],
        active_days = gi_data['stats']['active_day_number'],
        achievement = gi_data['stats']['achievement_number'],
        tower = gi_data['stats']['spiral_abyss'],
        theater = gi_data['stats']['role_combat']['max_round_id'],
        full_fetter_avatar = gi_data['stats']['full_fetter_avatar_num'],
        characters = gi_data['stats']['avatar_number'],
    )

    print(gi_user_info)

    hsr_uid = 801018449
    hsr_data = honkai_star_rail_user_info(hsr_uid)
    if hsr_data:
        print(hsr_data)
    else:
        print("Failed to get HSR user info")
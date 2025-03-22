import json
from os import getenv
from dotenv import load_dotenv
from dataclasses import dataclass
from utils import fetch_hoyo_data

@dataclass
class GenshinImpactUserInfo:
    """原神のユーザー情報を格納するデータクラス"""
    user_name: str                  # ユーザー名
    adventure_rank: int             # 冒険ランク
    active_days: int                # アクティブ日数
    achievement: int                # アチーブメント数
    tower: str                      # 深境螺旋
    theater: int                    # 幻想シアター
    full_fetter_avatar: int         # 好感度MAXキャラ数
    characters: int                 # キャラクター獲得数

@dataclass
class HonkaiStarRailUserInfo:
    """崩壊スターレイルのユーザー情報を格納するデータクラス"""
    user_name: str                  # ユーザー名
    active_days: int                # アクティブ日数
    achievement: int                # アチーブメント
    characters: int                 # キャラクター獲得数
    trailblaze_level: int           # 開拓者レベル
    frogotten_hall: int             # 忘却の庭
    pure_fiction: int               # 虚構叙事
    apocalyptic_shadow: int         # 末日の幻影

@dataclass
class ZenlessZoneZeroUserInfo:
    """ゼンレスゾーンゼロのユーザー情報を格納するデータクラス"""
    user_name: str                  # ユーザー名
    interknot_level: int            # インターノットレベル
    active_days: int                # アクティブ日数
    achievement: int                # アチーブメント数
    agents: int                     # エージェント獲得数
    bangboo: int                    # ポンプ獲得数
    deadly_assault: int             # 危局強襲戦
    shiyu_defense_frontier: int     # 式輿防衛戦
    hollow_zero_level: int          # 零号ホロウ

def genshin_user_info(uid: int) -> GenshinImpactUserInfo | None:
    """原神のユーザー情報を取得する"""
    data = fetch_hoyo_data("/game_record/genshin/api/index", uid, "os_asia")
    if not data:
        return None

    stats = data['stats']
    return GenshinImpactUserInfo(
        user_name=data['role']['nickname'],
        adventure_rank=data['role']['level'],
        active_days=stats['active_day_number'],
        achievement=stats['achievement_number'],
        tower=stats['spiral_abyss'],
        theater=stats['role_combat']['max_round_id'],
        full_fetter_avatar=stats['full_fetter_avatar_num'],
        characters=stats['avatar_number']
    )

def honkai_star_rail_user_info(uid: int) -> HonkaiStarRailUserInfo | None:
    """崩壊スターレイルのユーザー情報を取得する"""
    data = fetch_hoyo_data("/game_record/hkrpg/api/index", uid, "prod_official_asia", use_ds=True)
    if not data:
        return None

    stats = data['stats']
    avatars = data['avatar_list']
    trailblazer = next((a for a in avatars if 'suzu' in a['name']), None)
    
    return HonkaiStarRailUserInfo(
        user_name=trailblazer['name'] if trailblazer else avatars[0]['name'],
        active_days=stats['active_days'],
        achievement=stats['achievement_num'],
        characters=stats['avatar_num'],
        trailblaze_level=trailblazer['level'] if trailblazer else 1,
        frogotten_hall=stats.get('abyss_process', 0),
        pure_fiction=0,
        apocalyptic_shadow=0
    )

def zenless_zone_zero_user_info(uid: int) -> ZenlessZoneZeroUserInfo | None:
    """ゼンレスゾーンゼロのユーザー情報を取得する"""

    data = fetch_hoyo_data("/event/game_record_zzz/api/zzz/index", uid, "prod_gf_jp", use_ds=True, api_base="https://sg-public-api.hoyolab.com")

    # data = fetch_hoyo_data(
    #     "/event/game_record_zzz/api/zzz/index",
    #     uid,
    #     "prod_gf_jp",
    #     use_ds=True,
    #     api_base="https://sg-public-api.hoyolab.com"
    # )
    if not data:
        return None

    stats = data['stats']
    return ZenlessZoneZeroUserInfo(
        user_name="0",
        interknot_level=0,
        active_days=stats['active_days'],
        achievement=stats['achievement_count'],
        agents=stats['avatar_num'],
        bangboo=stats['buddy_num'],
        deadly_assault=0,
        shiyu_defense_frontier=stats['cur_period_zone_layer_count'],
        hollow_zero_level=0
    )

if __name__ == "__main__":
    load_dotenv()
    genshin_info = genshin_user_info(801870399)
    honkai_info = honkai_star_rail_user_info(802667063)
    zenless_info = zenless_zone_zero_user_info(1312835772)

    print(genshin_info)
    print(honkai_info)
    print(zenless_info)
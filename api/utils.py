import random
import hashlib
import string
import time
import requests
from os import getenv

def generate_ds():
    """DS（Dynamic Secret）を生成する"""
    salt = "6s25p5ox5y14umn1p61aqyyvbvvl3lrt"
    t = int(time.time())
    r = ''.join(random.choices(string.ascii_letters, k=6))
    h = hashlib.md5(f"salt={salt}&t={t}&r={r}".encode()).hexdigest()
    return f"{t},{r},{h}"

def fetch_hoyo_data(endpoint: str, uid: int, server: str, use_ds: bool = False, api_base: str = None) -> dict | None:
    """HoYoLAB APIからデータを取得する共通関数"""
    if api_base is None:
        api_base = "https://bbs-api-os.hoyolab.com"
    
    url = f"{api_base}{endpoint}"
    
    base_params = {
        "lang": "ja-jp",
        "game_biz": "hkrpg_jp" if "zzz" in endpoint else "hk4e_global",
        "region": "prod_gf_jp"
    }
    
    if "zzz" in endpoint:
        params = {"role_id": uid, "server": "prod_gf_jp", **base_params}
    else:
        params = {"role_id": uid, "server": server}

    # params = {"role_id": uid, "server": "prod_gf_jp" if "zzz" in endpoint else server, **base_params}
    
    headers = {
        "Cookie": f"ltoken_v2={getenv('HOYOLAB_LTOKEN')}; ltuid_v2={getenv('HOYOLAB_LTUID')};",
        "Origin": "https://act.hoyolab.com"
    }
    
    if use_ds:
        headers.update({
            "DS": generate_ds(),
            "x-rpc-client_type": "5",
            "x-rpc-app_version": "2.67.1",
            "x-rpc-language": "ja-jp",
            # "x-rpc-game_biz": base_params["game_biz"]
            "x-rpc-game_biz": "hkrpg_jp" if "zzz" in endpoint else "hk4e_global"
        })

    try:
        response = requests.get(url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data.get('data') if data.get('retcode') == 0 else None
    except Exception as e:
        print(f"Error fetching data: {e}")
    return None
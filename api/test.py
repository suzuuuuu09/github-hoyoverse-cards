import requests

def fetch_user_data(user_id: int):
    url = f"https://enka.network/api/uid/{user_id}?info"
    response = requests.get(url)
    if response.status_code != 200: return None
    data = response.json()
    user_name = data["playerInfo"]["nickname"]

    return user_name

if __name__ == "__main__":
    user_id = 800000000
    if user_name := fetch_user_data(user_id):
        print(user_name)
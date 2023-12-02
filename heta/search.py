import pprint
import requests

def search(query, limit=1, app_name="Heta lib"):
    return requests.get(
        "https://heta.hikariatama.ru/search",
        params={"q": query, "limit": limit},
        headers={
            "User-Agent": app_name,
        },
    ).json()
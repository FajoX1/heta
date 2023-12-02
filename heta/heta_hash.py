import pprint
import requests

def decode_hash(mhash, app_name="Heta lib"):
    return requests.get(
            "https://heta.hikariatama.ru/resolve_hash",
            params={"hash": mhash},
            headers={
                "User-Agent": app_name,
            },
        ).json()
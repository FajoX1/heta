import requests

def decode_hash(mhash, app_name="Heta lib"):
    return requests.get(
            "https://heta.dan.tatar/resolve_hash",
            params={"hash": mhash},
            headers={
                "User-Agent": app_name,
            },
        ).json()
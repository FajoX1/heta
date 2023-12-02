import requests

class repo():
    def get_modules(repo):
        mrepo = f"{repo}/raw/main/full.txt"
        response = requests.get(mrepo)
        if response.status_code != 200:
            return "no modules"
        modules = []
        modules = [{"name": name} for name in response.text.split('\n') if name.strip()]
        return modules
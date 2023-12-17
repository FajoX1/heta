import requests

class repo():
    def get_modules(repo):
        mrepo = f"{repo}/raw/main/full.txt"
        response = requests.get(mrepo)
        if response.status_code != 200:
            return "no modules"
        modules = []
        lines = response.text.split('\n')
        for name in lines:
            if name.strip():
                link = f"{repo}/raw/main/{name}.py"
                response = requests.get(link)
                if response.status_code == 200:
                      modules.append({"link": link, "name": name})

        if not modules:
            return "no modules"

        return modules

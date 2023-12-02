import requests

class module():
    def get_link(author, project_name, module_name):
        mlink = f"https://heta.hikariatama.ru/{author}/{project_name}/{module_name}.py"
        response = requests.get(mlink)
        if response.status_code != 200:
            return "not found"
        return mlink
    
    def get_code(mlink):
        response = requests.get(mlink)
        if response.status_code != 200:
            return "not found"
        return response.text
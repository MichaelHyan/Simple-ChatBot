import base64
import urllib
import requests
import json
import os
class speech_text():
    def __init__(self):
        with open('config.json','r',encoding='utf-8') as f:
            config = json.load(f)
        self.API_KEY = config['baidu_speech_API_KEY']
        self.SECRET_KEY = config['baidu_speech_SECRET_KEY']
        self.format = 'm4a'
    def to_text(self,path):
        url = "https://vop.baidu.com/server_api"
        payload_defalt = {
            "format": self.format,
            "rate": 16000,
            "channel": 1,
            "cuid": "n0Tl3d0TEQpQM6zrDokioodAXQWBNf5V",
            "speech": "",
            "len": 0,
            "token": self.get_access_token()
        }
        payload_defalt['speech'] = self.get_file_content_as_base64(path)
        payload_defalt['len'] = self.get_file_size(path)
        payload = json.dumps(payload_defalt, ensure_ascii=False)
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        response = requests.request("POST", url, headers=headers, data=payload.encode("utf-8"))
        
        response.encoding = "utf-8"
        response = response.json()
        return response['result'][0]
    def get_file_content_as_base64(self, path, urlencoded=False):
        with open(path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf8")
            if urlencoded:
                content = urllib.parse.quote_plus(content)
        return content

    def get_access_token(self):
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))
    
    def get_file_size(self,file_path):
        try:
            file_stats = os.stat(file_path)
            return file_stats.st_size
        except FileNotFoundError:
            print(f"文件不存在: {file_path}")
            return -1
        except Exception as e:
            print(f"读取文件时出错: {e}")
            return -1
def main():
    speech_text().to_text('audio.m4a')
if __name__ == '__main__':
    main()
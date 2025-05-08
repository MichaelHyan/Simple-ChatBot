#新版接口 支持创建多个对象 支持左右脑互博
import requests
import json

class pychatbot:
    def __init__(self,prompt=''):
        with open('config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
        self.API_KEY = config['ERNIE_API_KEY']
        self.SECRET_KEY = config['ERNIE_SECRET_KEY']
        self.prompt = self.prompt_set(prompt)
        self.prompt_ds = self.prompt_set(prompt)
        self.DS_key = config['DEEPSEEK_KEY']
        self.memory = {
                "model":"ernie-4.5-8k-preview",
                "messages": [],
                "temperature":0.95,
                "top_p":0.7,
                "penalty_score":1.0,
                "web_search": {
                    "enable": False,
                    "enable_citation": False,
                    "enable_trace": False
                    }
                }
        self.memory_ds = {
                "messages": [],
                "model": "deepseek-chat",
                "frequency_penalty": 0,
                "max_tokens": 2048,
                "presence_penalty": 0,
                "response_format": {
                    "type": "text"
                },
                "stop": None,
                "stream": False,
                "stream_options": None,
                "temperature": 1,
                "top_p": 1,
                "tools": None,
                "tool_choice": "none",
                "logprobs": False,
                "top_logprobs": None
                }
    #难道，今天会突然有个一米六，黑长直，看似高冷，外表却十分可爱，穿着jk，
    #是小时候很好的玩伴但是因为一些不可抗力分开了，在那之后他一直给我写信但是我因为某些原因没法收到，
    #今天在我写代码的时候，她带点傲娇小属性的同校小妹冲进教室里，用闪烁着泪花的眼睛和温柔细腻却带着一丝哭腔的声音，
    #深情的看着我并对我说：你从小代码写的就好，我喜欢你很久了，为什么还是察觉不到我。然后不顾班里同学的眼光一头趴进我怀里哭泣，
    #此时正好马上放学了，我直接把她带出学校仔细问问清楚，发现她现在家有五套房十辆车，
    #我们父亲互为同学，母亲是好闺蜜，紧接着更新了联系方式并与她拥抱，她的外表令现场所有男生女生羡慕，
    #她的超雄且健身对追求者此时赶来要和我决斗，最终被我在众目睽睽之下一拳撂倒，最终我们互相坚定的选择了对方
    #并许诺教她写一辈子代码

    def prompt_set(self,str):
        with open('prompts.json', 'r', encoding='utf-8') as f:
            prompts = json.load(f)
        try:
            p = prompts[str]
        except:
            p = str
        return p

    def get_access_token(self):
        try:
            url = "https://aip.baidubce.com/oauth/2.0/token"
            params = {"grant_type": "client_credentials", "client_id": self.API_KEY, "client_secret": self.SECRET_KEY}
            return str(requests.post(url, params=params).json().get("access_token"))
        except Exception as e:
            print(e)

    def md_clear(self,msg):
        msg = msg.replace('```', '').replace('#', '').replace('*', '').replace('\n\n','\n').replace('\n\n','\n')
        return msg
    
    def init(self):#让记忆消失的魔法
        self.memory = {
                "model":"ernie-4.5-8k-preview",
                "messages": [],
                "temperature":0.95,
                "top_p":0.7,
                "penalty_score":1.0,
                "web_search": {
                    "enable": False,
                    "enable_citation": False,
                    "enable_trace": False
                    }
                }
        self.memory_ds = {
                "messages": [],
                "model": "deepseek-chat",
                "frequency_penalty": 0,
                "max_tokens": 2048,
                "presence_penalty": 0,
                "response_format": {
                    "type": "text"
                },
                "stop": None,
                "stream": False,
                "stream_options": None,
                "temperature": 1,
                "top_p": 1,
                "tools": None,
                "tool_choice": "none",
                "logprobs": False,
                "top_logprobs": None
                }

    def reply(self,token,use_web = False):#文心一言用方法
        access_token=self.get_access_token()
        try:
            self.memory['messages'].append({'role':'user','content':token})
            if use_web:
                self.memory["web_search"]["enable"] = True
            if self.prompt != '' :
                self.memory['messages'][0]['content'] = f'{self.prompt}\n{token}'
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + access_token
            payload = json.dumps(self.memory,ensure_ascii=False)
            headers = {
            'Content-Type': 'application/json',
            }
            response = requests.request("POST", url, headers=headers, data=payload)
            result = response.json()['result'] 
            result = self.md_clear(result)
            self.memory['messages'].append({'role':'assistant','content':result})
            return result
        except Exception as e:
            return e
    def reply_ds(self,token):#deepseek用方法
        try:
            self.memory_ds['messages'].append({'role':'user','content':token})
            if self.prompt_ds != '' :
                self.memory_ds['messages'][0]['content'] = f'{self.prompt_ds}\n{token}'
            url = "https://api.deepseek.com/chat/completions"
            payload = json.dumps(self.memory_ds)
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': ''
            }
            headers['Authorization'] = f'Bearer {self.DS_key}'
            response = requests.request("POST", url, headers=headers, data=payload)
            result = response.json()['choices'][0]['message']['content']
            result = self.md_clear(result)
            self.memory_ds['messages'].append({'role':'assistant','content':result})
            return result
        except Exception as e:
            return e

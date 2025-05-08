import requests
import json
#旧版接口
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
API_KEY = config['ERNIE_API_KEY']
SECRET_KEY = config['ERNIE_SECRET_KEY']
DS_key = config['DEEPSEEK_KEY']
memory = []
def mem(str):
    if str == '':
        return str
    return f'用户以往的问题提到了“{str}”，这些内容可能和现在的问题相关，但不必去回答这些内容。'

def prompt_set(str):
        with open('prompts.json', 'r', encoding='utf-8') as f:
            prompts = json.load(f)
        try:
            p = prompts[str]
        except:
            p = ''
        return p

def get_access_token():
    try:
        url = "https://aip.baidubce.com/oauth/2.0/token"
        params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
        return str(requests.post(url, params=params).json().get("access_token"))
    except Exception as e:
        print(e)

def get_msg(token,prompt='',memory='',use_web = False,access_token=get_access_token()):
    prime = prompt_set(prompt) + mem(memory)
    if prompt != '' or memory != '':
        token = prime + f'\n以下是问题：\n' + token
    try:
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + access_token
        payload = json.dumps({
            "model":"ernie-4.5-8k-preview",
            "messages": [{
                "role": "user",
                "content": token
                }],
            "temperature":0.95,#控制回答的随机性，0-1，越大越随机
            "top_p":0.7,#控制回答的多样性，0-1，越大越多样
            "penalty_score":1.0,#重复惩罚 1-2（重复个屁 啥也记不住）
            #"stop":"",#生成到这个字符停止，只想让他答一句就写句号，别空着
            "web_search": {
                "enable": use_web,
                "enable_citation": False,
                "enable_trace": False
            },
            #"max_completion_tokens": #这玩意形同虚设
        },
        ensure_ascii=False)
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        #print(response.text)
        result = response.json()['result'] 
        result = md_clear(result)
        return result
    except Exception as e:
        return e

def md_clear(msg):
    msg = msg.replace('```', '').replace('#', '').replace('*', '').replace('\n\n','\n')
    return msg
def init():
    global memory
    memory = {
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
def c_memory(msg):
    global memory
    memory['messages'].append({'role':'assistant','content':msg})

def reply(token,prompt='',use_web = False,access_token=get_access_token()):
    global memory
    try:
        memory['messages'].append({'role':'user','content':token})
        if use_web:
            memory["web_search"]["enable"] = True
        if prompt != '' :
            memory['messages'][0]['content'] = f'{prompt_set(prompt)}\n{token}'
        url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + access_token
        payload = json.dumps(memory,ensure_ascii=False)
        headers = {
        'Content-Type': 'application/json',
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        result = response.json()['result'] 
        result = md_clear(result)
        c_memory(result)
        return result
    except Exception as e:
        return e
'''
def ds(token,prompt=''):
    client = OpenAI(api_key=DS_key, base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": token},
        ],
        stream=False
    )
    return response.choices[0].message.content
'''
if __name__ == '__main__':
    init()
    print('###############################################')
    while True:
        a = input()
        if a == 'exit':
            break
        elif a == 'reset':
            init()
        else:
            print('###############################################')
            print(reply(a,use_web=True))
            print('###############################################')
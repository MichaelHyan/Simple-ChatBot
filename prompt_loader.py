import json,time
print('将人设文本文档拖至此处')
path = input()
with open(path, 'r', encoding='utf-8') as f:
    p = f.read()
p = p.replace('\n','\\n')
with open('prompts.json','r',encoding='utf-8') as f:
    pr = json.load(f)
name = path.split('\\')[-1].split('.')[0]
pr[name] = p
with open('prompts.json','w',encoding='utf-8') as f:
    json.dump(pr,f,ensure_ascii=False)
with open('config.json','r',encoding='utf-8') as f:
    c = json.load(f)
c['prompt_list'].append(name)
with open('config.json','w',encoding='utf-8') as f:
    json.dump(c,f,ensure_ascii=False)
print('人设已加载')
time.sleep(3)
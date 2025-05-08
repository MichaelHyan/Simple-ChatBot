# Simple-ChatBot
## 一个简单的聊天机器人实例
### 功能
对话能力（目前支持文心一言和deepseek）

对话框

live2D角色展示（可更换）

嘴型模拟

语音回复

### 环境
python 3.8以上

必要库
```bash
pip install -r requirements.txt
```
### 部署方式

申请deepseek或文心一言密钥

deepseek开放平台
> https://platform.deepseek.com/

申请后仅能查看一次密钥，请妥善保存



千帆大模型控制台
> https://console.bce.baidu.com/

获取后在项目根目录config.json文件中以下位置填写密钥


```
"ERNIE_API_KEY":"",       #文心一言api key
"ERNIE_SECRET_KEY":"",    #文心一言secret ket
"DEEPSEEK_KEY":"",        #deepseek api key
```

#### 运行
本地运行

使用start.bat或在终端运行
```bash
python chatbot.py
```
启动后将自动弹出webui

### 对话设置
#### 语音
可以手动关闭语音功能

在对话框输入以下指令控制语音开/关

```
#voice set on
#voice set off
```
#### 更换人设
人设可在prompts.json中编辑

在文件中加入以下内容

```
"你的人设名":"你的人设"
```
同时在config.json中更改人设
```
"prompt":"你的人设",
```
或者直接运行prompt_loader.py

将人设文本放入任意文本文件，并把文件拖到prompt_loader.py中，运行即可

人设默认为增强版猫娘，由zzZZSTstt(调教)编辑

更换模型

支持json格式live2D模型

默认模型来源：模之屋 【免费模型】O13

可自行更改

下载模型后将config.json中的路径指定到新模型

```
"model_path":".\\live2d\\MAOMAO\\MAOMAO.model3.json"
```

#### 声音
暂时使用edge_tts 的zh-CN-XiaoyiNeurral

由于so-vits-svc等消耗性格过大(我电脑带不动)，暂时未加入声音克隆功能

### 独立功能
pychatbot.py可作为独立模块使用

默认拥有记忆功能

api key等获取和设置方式同上

对话对象创建

```
bot = pychatbot.pychatbot('你的人设，不填也行')
```
对话记忆清空

```
bot.init()
```
获取返回信息

```
print(bot.reply('发送的信息'))   #文心一言模式
print(bot.reply('发送的信息'))   #deepseek模式
```
两种模式互不干扰，~~可以左右脑互博~~，根据需要调用

### 其他
界面在后续更新中可能更改
# Simple-ChatBot
## 一个简单的聊天机器人实例
### 功能
对话能力（目前支持文心一言和deepseek）

对话框

live2D角色展示（可更换）

嘴型模拟

语音回复

### 原理

使用API接入文心一言或deepseek

tts功能来自edge_tts

前端由gradio和pygame live2d-py处理

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

人设默认为增强版猫娘，由zzZZSTstt~~调教~~编辑

#### 更换模型

支持json格式live2D模型

默认模型来源：模之屋 【免费模型】O13

可自行更改

下载模型后将config.json中的路径指定到新模型

```
"model_path":".\\live2d\\MAOMAO\\MAOMAO.model3.json"
```

#### 更换背景

将待更改图片转换为400*500的尺寸

放入.\\pic\\文件夹

修改config.json

```
"background_path":".\\pic\\",       #为了稳定尽量放这，别的地方也行
"background":"bak0.jpg",            #改成你的图片的名字
```

zzst批注：在 live2d-py 项目的图像加载模块中，存在纹理坐标处理不一致的问题：当加载 PNG 格式图像时，由于未对纹理坐标的 Y 轴进行垂直翻转（仅针对 JPEG 格式实现了坐标校正），会导致渲染结果出现垂直镜像现象（zzst恍然大明白）。该问题的技术本质源于不同图像格式在图形 API 中的纹理坐标方向差异（PNG 采用自上而下的坐标系统，而 OpenGL 等图形接口通常使用自下而上的纹理坐标系）。如需解决此问题，可参考我针对该模块的纹理坐标处理逻辑修改方案，通过增加对 PNG 格式的垂直翻转处理来实现多格式图像的正确渲染。

Hyan批注：PYPi的live2d-py目前没有处理图像的模块，建议去原作者项目的.\\package\\live2d找，或者直接用本项目的。

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
print(bot.reply_ds('发送的信息'))   #deepseek模式
```
两种模式互不干扰，~~可以左右脑互博~~，根据需要调用

### 其他
界面在后续更新中可能更改
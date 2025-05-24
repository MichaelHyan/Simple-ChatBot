'''chatbot v1.3.2'''
import gradio as gr
import ernie_bot,pygame, time,tts,threading,pychatbot
import live2d_test
import waver,webbrowser,json
config = json.load(open('config.json','r',encoding='utf-8'))
#ernie_bot.init()
bot = pychatbot.pychatbot(config['prompt'])
bot.init()
def play_audio(stop_audio):
    try:
        live2d_test.vol = 1
        pygame.mixer.init()
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        pygame.mixer.quit()
        live2d_test.vol = 0
    except:
        pass
stop_audio = threading.Event()
audio = True
def random_response(message, history):
    global audio,bot
    try:
        stop_audio.set()
        if message[0] == '#':
            if message == '#init':
                bot.init()
                return f'[info]记忆已初始化'
            if message == '#voice on':
                audio = True
                return f'[info]语音已启用'
            if message == '#voice off':
                audio = False
                return f'[info]语音已关闭'
            if message == '#mem list':
                return f'[info]记忆列表:\n{bot.memory_list()}'
            if message == '#trace on':
                live2d_test.trace = True
                return f'[info]视线跟踪已启用'
            if message == '#trace off':
                live2d_test.trace = False
                return f'[info]视线跟踪已关闭'
            if '#mem save' in message:
                message = message.split(' ')[-1]
                bot.memory_save(message)
                return f'[info]记忆[{message}]已保存'
            if '#mem load' in message:
                message = message.split(' ')[-1]
                if bot.memory_load(message):
                    return f'[info]记忆[{message}]已加载'
                else:
                    return f'[info]记忆加载失败'
            else:
                return f'[info]未知命令'
        if 'ciallo' in message or 'Ciallo' in message or 'CIALLO' in message:
            return f'[info]来人把柚子厨叉出去'
        #msg = ernie_bot.get_msg(message,prompt='neko')#旧接口
        #msg = ernie_bot.reply(message,prompt='neko',use_web=True)
        if config['model'] == 'deepseek':
            msg = bot.reply_ds(message)
        elif config['model'] == 'ernie_bot':
            msg = bot.reply(message)
        msga = clar(msg)
        if audio:
            tts.bake(str(msga),offset=4)
            live2d_test.wav = waver.get_wave()
            thread = threading.Thread(target=play_audio,args=(stop_audio,))
            thread.start()
        return msg
    except Exception as e:
        return f'错误信息:\n{e}'
def clar(msg):
    temp = ''
    k = 1
    for i in msg:
        if i == '（' or i == '(':   
            k = 0
        if k == 1:
            temp += i
        if i == '）' or i == ')':
            k = 1
            temp += '。'
    msg = temp
    return msg
webbrowser.open('http://127.0.0.1:7860')
threading.Thread(target=live2d_test.main).start()
gr.ChatInterface(
    fn=random_response, 
    type="messages",
).launch()

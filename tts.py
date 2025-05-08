#voice_offset预设：1童声 2男声低 3男声高 4女声低 5女声高
#参数：tts.bake(文本，路径，预设)
#路径预设为output.mp4，声音预设为男声高，可以再改
import edge_tts
import asyncio
async def tts(text,path,offset):
    voice_offset = ['zh-CN-YunxiaNeural','zh-CN-YunyangNeural','zh-CN-YunxiNeural','zh-CN-XiaoxiaoNeural','zh-CN-XiaoyiNeural']
    voice = voice_offset[offset]
    output_file = path
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_file)
def bake(text,path='output.mp3',offset=2):
    asyncio.run(tts(text,path,offset))
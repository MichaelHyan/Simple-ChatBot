import os
import subprocess
def convert_wav_to_m4a(input_file, output_file, ffmpeg_path):

    try:
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"输入文件不存在: {input_file}")
        if not os.path.exists(ffmpeg_path):
            raise FileNotFoundError(f"ffmpeg不存在: {ffmpeg_path}")
        command = [
            ffmpeg_path,
            '-i', input_file,
            '-c:a', 'aac',
            '-b:a', '192k',
            '-y',
            output_file
        ]
        subprocess.run(command, check=True)
        print(f"转换成功: {output_file}")
        
    except subprocess.CalledProcessError as e:
        print(f"转换失败: {str(e)}")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def convert():
    convert_wav_to_m4a("audio.wav", "audio.m4a", '.\\ffmpeg\\bin\\ffmpeg.exe')

if __name__ == '__main__':
    input_wav = 'audio.wav'
    output_m4a = 'audio.m4a'
    ffmpeg_location = '.\\ffmpeg\\bin\\ffmpeg.exe'
    convert_wav_to_m4a(input_wav, output_m4a, ffmpeg_location)

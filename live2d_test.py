import math,json,os,pygame
import waver
from pygame.locals import *
import live2d.v3 as live2d
from live2d.v3 import StandardParams
from live2d.utils.image import Image
with open('config.json',encoding='utf-8') as f:
    config = json.load(f)
path = config['model_path']
bak = config['background_path']+config['background']
live2d.setLogEnable(False)
vol = 0
wav = []
#wav = waver.get_wave_max()
def main():
    global vol,wav
    pygame.init()
    pygame.mixer.init()
    live2d.init()
    display = (500, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("pygame window")
    if live2d.LIVE2D_VERSION == 3:
        live2d.glewInit()
    model = live2d.LAppModel()
    model.LoadModelJson(os.path.join(path))
    model.Resize(*display)
    running = True
    dx: float = 0.0
    dy: float = 0.0
    scale: float = 1.0
    model.SetAutoBlinkEnable(True)
    model.SetAutoBreathEnable(True)
    background = Image(os.path.join(bak))
    fc = None
    sc = None
    model.StartRandomMotion("TapBody", 30, sc, fc)
    progress = 0
    check = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                model.StartRandomMotion(priority=3)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx -= 0.1
                elif event.key == pygame.K_RIGHT:
                    dx += 0.1
                elif event.key == pygame.K_UP:
                    dy += 0.1
                elif event.key == pygame.K_DOWN:
                    dy -= 0.1
                elif event.key == pygame.K_i:
                    scale += 0.1
                elif event.key == pygame.K_u:
                    scale -= 0.1
                elif event.key == pygame.K_r:
                    model.StopAllMotions()
                    model.ResetPose()
                elif event.key == pygame.K_e:
                    model.ResetExpression()

            if event.type == pygame.MOUSEMOTION:
                model.Drag(*pygame.mouse.get_pos())
        if not running:
            break
        model.Update()
        if vol == 1:
            try:
                if wav[check] >= 0.1:
                    model.SetParameterValue(
                    StandardParams.ParamMouthOpenY, math.sin(progress/3)*0.5
                    )
                else:
                    model.SetParameterValue(
                        StandardParams.ParamMouthOpenY, 0
                    )
                check += 1
            except Exception as e:
                check = 0
                vol = 0
                print(e)
            
        if vol == 0:
            model.SetParameterValue(
                StandardParams.ParamMouthOpenY, 0
            )
            check = 0

        model.SetOffset(dx, dy)
        model.SetScale(scale)        
        live2d.clearBuffer(1,1,1,0)
        background.Draw()
        model.Draw()
        pygame.display.flip()
        pygame.time.wait(10)
        progress += 1

if __name__ == "__main__":
    currentTopClickedPartId = None
    main()
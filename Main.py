import os
import pygame
import live2d.v3 as live2d
#import live2d.v2 as live2d

from live2d.utils.image import Image
#wav = waver.get_wave_max()
def main():
    pygame.init()
    pygame.mixer.init()
    live2d.init()
    display = (500, 600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)
    pygame.display.set_caption("pygame window")
    live2d.glewInit()

    running = True
    background = Image(
        os.path.join(".\\poster.jpg")
        )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        if not running:
            break
        live2d.clearBuffer()
        background.Draw()
        pygame.display.flip()
    live2d.dispose()
    live2d.quit()

if __name__ == "__main__":
    main()
import pygame
import image
import time
import PIL.ImageOps

file = "anseladams"

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pil_im = image.open_image(f"./images/{file}.jpg")
screen_size = pil_im.size
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
pil_im = image.apply_dither_rgb(pil_im)
screen.fill("purple")
pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
screen.blit(pyg_im, (0,0))
pygame.display.flip()
clock.tick(60)

#pil_im = PIL.ImageOps.invert(pil_im) <---swap live and dead cells

gen_ct = 0
print(f"gen:{str(gen_ct)}")
start = time.time()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pil_im = image.apply_filter_rgb(pil_im, 1, "dead")
    pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
    gen_ct += 1
    print(f"gen:{str(gen_ct)} time diff:{str(time.time() - start)}")
    start = time.time()
    screen.blit(pyg_im, (0,0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

#save image as a BMP when window closed (jpeg is too lossy)
pygame.image.save(pyg_im, f"{file}_gen{gen_ct}.bmp")
pygame.quit()
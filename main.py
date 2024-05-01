import pygame
import image

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
pil_im = image.open_image("./images/tripod.jpg")
screen_size = pil_im.size
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
pil_im = image.apply_dither(pil_im)
screen.fill("purple")
pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
screen.blit(pyg_im, (0,0))
pygame.display.flip()
clock.tick(60)

gen_ct = 0
print(gen_ct)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pil_im = image.apply_filter(pil_im, 1, "dead")
    pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
    gen_ct += 1
    print(gen_ct)
    screen.blit(pyg_im, (0,0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

#save image as a BMP when window closed (jpeg is too lossy)
pygame.image.save(pyg_im, f"tripod_gen{gen_ct}.bmp")
pygame.quit()
import pygame
import image

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
pil_im = image.open_image("./images/snake.jpg")
pil_im = image.apply_dither(pil_im)
screen.fill("purple")
pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
screen.blit(pyg_im, (0,0))


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    pil_im = image.apply_filter(pil_im, 3, "dead")
    #BUG: using different generation counts yields different results after the same total number of generations
    #I think it's from apply filter, since the image does not need to be ditehred every time
    pyg_im = pygame.image.frombytes(pil_im.convert("RGB").tobytes(), pil_im.size, "RGB").convert()
    screen.blit(pyg_im, (0,0))


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
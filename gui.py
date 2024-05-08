import pygame as pg
import pygame_gui as gui



# pygame setup
pg.init()
bg_color = "gray60"
scr_size = pg.display.get_desktop_sizes()[0]
scr_flags = pg.RESIZABLE 
screen = pg.display.set_mode(scr_size, flags=scr_flags)
image = pg.image.load("images/spongebob.jpg").convert()
manager = gui.UIManager(scr_size)


hello_button = gui.elements.ui_selection_list.UISelectionList(
                relative_rect=pg.Rect((350, 275), (100, 500)),
                item_list=("a","b","C"),
                allow_double_clicks=False,
                manager=manager)


def my_stuff(img): 
    screen.fill(bg_color)
    size = pg.display.get_window_size()
    offset = 25

    box = pg.Surface((size[0]-500, size[1]-2*offset))
    box.fill("gray40")
    box_rect = box.get_rect()
    box_rect.move_ip(offset, offset)

    img_scale = (box_rect.w-offset, box_rect.h-offset)
    img = pg.transform.scale(img, img_scale)
    img_rect = image.get_rect(center=box_rect.center)
    img_rect.center = box_rect.center

    box.blit(img, img_rect)
    screen.blit(box, box_rect)


#Here is a very standard loop that includes only one line to update UI elements.
clock = pg.time.Clock()
running = True
while running:
    #clock.tick(60)
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == gui.UI_BUTTON_PRESSED:
            if event.ui_element == hello_button:
                print('Hello World!')
        manager.process_events(event)

    manager.update(time_delta)
    my_stuff(image) #do your stuff with display
    manager.draw_ui(screen)
    pg.display.update()
pg.quit()

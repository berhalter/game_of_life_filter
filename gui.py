import pygame as pg
import pygame_gui as gui
import game


# pygame setup
pg.init()
bg_color = "gray60"
scr_size = pg.display.get_desktop_sizes()[0]
scr_flags = pg.RESIZABLE 
screen = pg.display.set_mode(scr_size, flags=scr_flags)
image = pg.image.load("images/snake.jpg").convert()



#gui elements
manager = gui.UIManager(scr_size)
panel_size = 200
offset = 10

pad_mode = "dead"
pad_mode_dropdown = gui.elements.ui_drop_down_menu.UIDropDownMenu(
    options_list=("dead","live","wrap","symmetric"),
    starting_option=pad_mode,
    relative_rect=pg.Rect((offset,offset), (125, 25)),
    manager=manager
)

gen_ct = 10
gen_text_entry = gui.elements.ui_text_entry_line.UITextEntryLine(
    relative_rect=pg.Rect((0,0), (125, 25)),
    manager=manager,
    anchors={'top': 'top',
             'right': 'right',
             'top_target': pad_mode_dropdown,
             'right_target': pad_mode_dropdown},
    initial_text=str(gen_ct),
    placeholder_text="Enter a number" 
)
gen_text_entry.set_allowed_characters("numbers")

dither_mode="2x2"
dither_dropdown = gui.elements.ui_drop_down_menu.UIDropDownMenu(
    options_list=("2x2","4x4","8x8"),
    starting_option=dither_mode,
    relative_rect=pg.Rect((0,0), (125, 25)),
    manager=manager,
    anchors={'top': 'top',
             'right': 'right',
             'top_target': gen_text_entry,
             'right_target': gen_text_entry} 
)

label = gui.elements.ui_label.UILabel(
    relative_rect=pg.Rect((0,0), (125, 25)),
    manager=manager,
    text="label text",
    anchors={'top': 'top',
             'right': 'right',
             'top_target': dither_dropdown,
             'right_target': dither_dropdown} 
)

button = gui.elements.ui_button.UIButton(
    relative_rect=pg.Rect((0,0), (125, 25)),
    manager=manager,
    text="button text",
    tool_tip_text="tool tip text",
    anchors={'top': 'top',
             'right': 'right',
             'top_target': label,
             'right_target': label} 
)

#shamelessly taken from https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
def img_scale_keep_ratio(img, box_size):
    img_width, img_height = img.get_size()
    scale = min(box_size[0] / img_width, box_size[1] / img_height)
    new_size = (round(img_width * scale), round(img_height * scale))
    scaled_img = pg.transform.scale(img, new_size) 
    img_rect = scaled_img.get_rect(center = (box_size[0] // 2, box_size[1] // 2))
    return scaled_img, img_rect

def draw_image(img): 
    screen.fill(bg_color)
    size = pg.display.get_window_size()

    box = pg.Surface((size[0]-panel_size, size[1]-2*offset))
    box.fill("gray40")
    box_rect = box.get_rect()
    box_rect.move_ip(size[0]-box_rect.size[0]-offset, offset)

    img, img_rect = img_scale_keep_ratio(img, box.get_size())
    box.blit(img, img_rect)
    screen.blit(box, box_rect)


clock = pg.time.Clock()
running = True
while running:
    #clock.tick(60)
    time_delta = clock.tick(60)/1000.0
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # if event.type == pg.VIDEORESIZE:
        #     pass
        if event.type == gui.UI_DROP_DOWN_MENU_CHANGED:
            if event.ui_element == pad_mode_dropdown:
                pad_mode = event.text
                print(f"Padding option: {pad_mode}")
            if event.ui_element == dither_dropdown:
                dither_mode = event.text
                print(f"Dither option: {dither_mode}")
        if event.type == gui.UI_TEXT_ENTRY_CHANGED:
            if event.ui_element == gen_text_entry:
                ngens = int(event.text)
                print(f"Number of gens: {ngens}")
        if event.type == gui.UI_BUTTON_PRESSED:
            if event.ui_element == button:
                pad_mode_dropdown.disable()
                dither_dropdown.disable()
                gen_text_entry.disable()
                button.disable()
                print("Button!")
        manager.process_events(event)

    manager.update(time_delta)
    draw_image(image)
    manager.draw_ui(screen)
    pg.display.flip()
pg.quit()

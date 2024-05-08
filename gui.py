import pygame
import random
import thorpy as tp

# pygame setup
pygame.init()
bg_color = "lightslategray"
screen_w, screen_h = 1200, 700
screen = pygame.display.set_mode((screen_w, screen_h))


def my_stuff(): #do what you want with the display like in any pygame code you write
    screen.fill(bg_color)

#Now let's pretend the UI elements below are what you need for your app:
tp.init(screen, tp.theme_classic)

buttons1 = [tp.Button("Group1-"+str(i)) for i in range(10)]
#give random pos for each button, since we did not sort them so far
for b in buttons1:
    b.set_topleft(x=random.randint(0,300), y=random.randint(100,screen_h-100))
group1 = tp.Group(buttons1,None) #group elements without sorting them

#group with vertically sorted elements
group2 = tp.Group([tp.Button("Group2-"+str(i)) for i in range(10)], "v")

#group with horizontally sorted elements
group3 = tp.Group([tp.Button("Group3-"+str(i)) for i in range(10)], "h")
group3.stick_to(screen, "top", "top", delta=(0,5))

#group with a grid of 2x5 elements.
group4 = tp.Group([tp.Button("Group4-"+str(i)) for i in range(10)], None)
group4.sort_children("grid", nx=2, ny=5)
group4.stick_to(screen, "right", "right", delta=(-5,0))

#group the groups.
final_group = tp.Group([group1,group2,group3,group4], None)
updater = final_group.get_updater() #this will be used to update the UI elements

#Here is a very standard loop that includes only one line to update UI elements.
clock = pygame.time.Clock()
playing = True
while playing:
    clock.tick(60)
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            playing = False
        else:
            ... #do your stuff with events
    my_stuff() #do your stuff with display

    #update Thorpy elements and draw them
    updater.update(events=events)
    pygame.display.flip()
pygame.quit()

from pygame import image, transform, display


#загрузка фонов
bg= []

bg.append(image.load("background/plx-1.png"))
bg.append(image.load("background/plx-2.png"))
bg.append(image.load("background/plx-3.png"))
bg.append(image.load("background/plx-4.png"))
bg.append(image.load("background/plx-5.png"))

SCALE = 3
HIGH = bg[1].get_height() * SCALE
SIZE = bg[1].get_width()  * SCALE

gamedisplay = display.set_mode((SIZE, HIGH))
display.set_caption("Jungle")

for i in range (len(bg)):
    bg[i] = transform.scale(bg[i].convert_alpha(), (SIZE, HIGH))


def show_background():
    for img in bg:
        gamedisplay.blit(img, (0,0))


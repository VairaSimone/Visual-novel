"""Generate original atmospheric prototype backgrounds for the Ren'Py project.

These assets are deliberately abstract and contain no likenesses of the
reference images. Re-run this script whenever a clean prototype set is needed.
"""

from pathlib import Path
from random import Random

from PIL import Image, ImageDraw, ImageFilter


WIDTH, HEIGHT = 1920, 1080
OUT = Path(__file__).parents[1] / "La bambola della porta accanto" / "game" / "images" / "backgrounds"
RNG = Random(4082)


def gradient(top, bottom):
    image = Image.new("RGB", (WIDTH, HEIGHT))
    pixels = image.load()
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        color = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(WIDTH):
            grain = RNG.randrange(-3, 4)
            pixels[x, y] = tuple(max(0, min(255, channel + grain)) for channel in color)
    return image


def glow(image, center, radius, color):
    layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=color)
    return Image.alpha_composite(image.convert("RGBA"), layer.filter(ImageFilter.GaussianBlur(radius // 2)))


def rain(draw, count=145):
    for _ in range(count):
        x = RNG.randrange(WIDTH)
        y = RNG.randrange(HEIGHT)
        length = RNG.randrange(14, 38)
        draw.line((x, y, x - length // 3, y + length), fill=(180, 190, 210, RNG.randrange(22, 60)), width=2)


def house(draw, x, y, width, height, lit=False):
    roof = [(x - 35, y), (x + width // 2, y - 135), (x + width + 35, y)]
    draw.polygon(roof, fill=(20, 20, 27, 255))
    draw.rectangle((x, y, x + width, y + height), fill=(27, 28, 34, 255))
    draw.rectangle((x + width * .42, y + height * .37, x + width * .58, y + height), fill=(13, 15, 20, 255))
    for wx in (x + width * .16, x + width * .67):
        for wy in (y + height * .24, y + height * .58):
            fill = (212, 172, 99, 255) if lit else (43, 47, 56, 255)
            draw.rectangle((wx, wy, wx + width * .15, wy + height * .18), fill=fill)
            draw.line((wx + width * .075, wy, wx + width * .075, wy + height * .18), fill=(48, 42, 39, 180), width=3)
            draw.line((wx, wy + height * .09, wx + width * .15, wy + height * .09), fill=(48, 42, 39, 180), width=3)


def save(image, name):
    OUT.mkdir(parents=True, exist_ok=True)
    image.convert("RGB").save(OUT / name, quality=94)


def title():
    image = gradient((11, 8, 16), (38, 24, 37)).convert("RGBA")
    image = glow(image, (1470, 355), 190, (126, 74, 86, 48))
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 725, WIDTH, HEIGHT), fill=(9, 11, 15, 220))
    house(draw, 985, 510, 370, 390, True)
    house(draw, 1420, 510, 370, 390, False)
    draw.rectangle((0, 885, WIDTH, HEIGHT), fill=(12, 20, 21, 255))
    draw.line((0, 888, WIDTH, 888), fill=(92, 80, 88, 100), width=3)
    rain(draw, 190)
    save(image, "title_night.jpg")


def mila_room():
    image = gradient((25, 22, 30), (65, 48, 58)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 0, 1120, HEIGHT), fill=(41, 36, 46, 255))
    draw.rectangle((1260, 110, 1780, 690), fill=(16, 23, 35, 255))
    for y in range(130, 680, 60):
        draw.line((1260, y, 1780, y), fill=(89, 101, 120, 45), width=2)
    draw.rectangle((1270, 700, 1770, 720), fill=(76, 53, 54, 255))
    draw.rectangle((150, 630, 1010, 930), fill=(30, 25, 31, 255))
    draw.rectangle((185, 590, 980, 710), fill=(161, 150, 151, 255))
    draw.rectangle((185, 710, 980, 910), fill=(69, 57, 72, 255))
    draw.rectangle((80, 120, 680, 490), outline=(130, 115, 130, 130), width=8)
    draw.rectangle((205, 190, 505, 450), fill=(29, 25, 32, 255))
    draw.rectangle((545, 190, 640, 450), fill=(145, 124, 120, 100))
    image = glow(image, (470, 320), 120, (218, 174, 133, 20))
    save(image, "mila_room.jpg")


def mila_kitchen():
    image = gradient((49, 38, 39), (18, 19, 25)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 0, WIDTH, 210), fill=(31, 29, 33, 255))
    for x in range(0, WIDTH, 320):
        draw.rectangle((x + 12, 30, x + 300, 190), fill=(57, 47, 48, 255), outline=(110, 88, 80, 120), width=4)
    draw.rectangle((0, 610, WIDTH, 770), fill=(72, 59, 57, 255))
    draw.rectangle((0, 770, WIDTH, HEIGHT), fill=(24, 24, 29, 255))
    draw.rectangle((1240, 325, 1510, 590), fill=(25, 24, 29, 255))
    draw.ellipse((1320, 410, 1420, 510), outline=(176, 163, 158, 150), width=8)
    draw.line((1370, 510, 1370, 590), fill=(176, 163, 158, 150), width=8)
    draw.rectangle((400, 560, 750, 625), fill=(31, 30, 34, 255))
    image = glow(image, (540, 410), 190, (218, 174, 118, 54))
    save(image, "mila_kitchen.jpg")


def school():
    image = gradient((77, 83, 102), (23, 29, 39)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 480, WIDTH, 900), fill=(50, 54, 64, 255))
    draw.rectangle((160, 275, 1510, 590), fill=(38, 43, 52, 255))
    for x in range(245, 1440, 185):
        for y in (330, 430):
            draw.rectangle((x, y, x + 95, y + 58), fill=(147, 155, 164, 110))
    draw.rectangle((770, 425, 980, 590), fill=(19, 25, 31, 255))
    draw.polygon([(0, 780), (WIDTH, 735), (WIDTH, HEIGHT), (0, HEIGHT)], fill=(25, 29, 36, 255))
    rain(draw, 115)
    save(image, "school.jpg")


def oak_and_houses():
    image = gradient((11, 22, 32), (31, 26, 35)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    image = glow(image, (1460, 220), 130, (191, 154, 100, 28))
    draw = ImageDraw.Draw(image, "RGBA")
    house(draw, 160, 490, 465, 430, True)
    house(draw, 1290, 490, 465, 430, False)
    draw.rectangle((0, 880, WIDTH, HEIGHT), fill=(13, 25, 25, 255))
    draw.line((0, 875, WIDTH, 875), fill=(105, 107, 103, 60), width=4)
    draw.line((956, 1030, 980, 280), fill=(20, 17, 20, 255), width=84)
    branches = [(970, 450, 720, 285), (970, 510, 1190, 280), (955, 370, 840, 130), (985, 410, 1320, 150), (900, 300, 650, 110), (1100, 300, 1480, 75)]
    for branch in branches:
        draw.line(branch, fill=(18, 16, 20, 255), width=42)
    for _ in range(120):
        x = RNG.randrange(470, 1530)
        y = RNG.randrange(35, 420)
        r = RNG.randrange(12, 37)
        draw.ellipse((x-r, y-r, x+r, y+r), fill=(18, 29, 31, RNG.randrange(120, 230)))
    rain(draw, 210)
    save(image, "oak_houses.jpg")


def sophie_kitchen():
    image = gradient((38, 33, 27), (15, 17, 21)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 0, WIDTH, 270), fill=(50, 43, 37, 255))
    for x in range(100, 1740, 420):
        draw.rectangle((x, 35, x + 330, 238), fill=(70, 60, 51, 255), outline=(116, 96, 76, 100), width=4)
    draw.rectangle((0, 575, WIDTH, 720), fill=(108, 97, 87, 255))
    draw.rectangle((0, 720, WIDTH, HEIGHT), fill=(24, 24, 27, 255))
    draw.rectangle((1000, 410, 1510, 585), fill=(34, 32, 31, 255))
    draw.ellipse((1195, 435, 1345, 545), fill=(36, 40, 41, 255), outline=(155, 147, 130, 150), width=5)
    draw.rectangle((1165, 535, 1375, 560), fill=(41, 42, 42, 255))
    image = glow(image, (620, 380), 230, (229, 190, 126, 56))
    save(image, "sophie_kitchen.jpg")


def bedroom_sophie():
    image = gradient((20, 24, 31), (61, 37, 52)).convert("RGBA")
    draw = ImageDraw.Draw(image, "RGBA")
    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=(22, 24, 31, 255))
    draw.rectangle((80, 100, 640, 800), fill=(48, 39, 54, 255))
    draw.rectangle((1260, 125, 1770, 670), fill=(13, 21, 31, 255))
    draw.line((1515, 125, 1515, 670), fill=(115, 125, 150, 80), width=5)
    draw.line((1260, 398, 1770, 398), fill=(115, 125, 150, 80), width=5)
    draw.rectangle((840, 700, 1820, 960), fill=(28, 25, 31, 255))
    draw.rectangle((870, 650, 1780, 755), fill=(150, 130, 142, 180))
    for _ in range(16):
        x = RNG.randrange(110, 570)
        y = RNG.randrange(130, 740)
        draw.rectangle((x, y, x + RNG.randrange(45, 110), y + RNG.randrange(65, 155)), outline=(176, 136, 158, 140), width=3)
    image = glow(image, (1450, 270), 160, (141, 104, 155, 38))
    save(image, "sophie_room.jpg")


if __name__ == "__main__":
    title()
    mila_room()
    mila_kitchen()
    school()
    oak_and_houses()
    sophie_kitchen()
    bedroom_sophie()
    print(f"Created prototype backgrounds in {OUT}")

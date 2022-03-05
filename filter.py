from PIL import Image, ImageDraw, ImageFont
import random


def edit(msg):
    son = random.randint(1,32)
    img = Image.open(f"imgs/{son}.jpg")
    img_draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype("fonts/Lobster-Regular.ttf", size=95)

    w, h = img_draw.textsize(msg,fnt)

    img_draw.text(((img.width - w) / 2,(img.height - h) / 1 - 10), f"“{msg}”", font=fnt)

    rtr = f"new_imgs/{msg}.jpg"
    img.save(rtr)
    return rtr

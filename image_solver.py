from PIL import Image

import io
import math

# js draw_image
def draw_image(dest, src, dest_x, dest_y, dest_width, dest_height, src_x, src_y, src_width, src_height):
    src_rect = src.crop((src_x, src_y, src_x + src_width, src_y + src_height))
    src_rect.resize((dest_width, dest_height), Image.ANTIALIAS)
    dest.paste(src_rect, (dest_x, dest_y, dest_x + dest_width, dest_y + dest_height))
    return dest

def solve(image_data):
    original = Image.open(io.BytesIO(image_data))

    keys = original.getexif()[0xa420]
    y = keys.split(":")

    x = original.width - 90
    v = original.height - 140
    b = math.floor(x / 10)
    w = math.floor(v / 15)

    new = Image.new(original.mode, (x, v))

    new = draw_image(new, original, 0, 0, x, w, 0, 0, x, w)
    new = draw_image(new, original, 0, w, b, v - 2 * w, 0, w + 10, b, v - 2 * w)
    new = draw_image(new, original, 0, 14 * w, x, original.height - 14 * (w + 10), 0, 14 * (w + 10), x, original.height - 14 * (w + 10))
    new = draw_image(new, original, 9 * b, w, b + (x - 10 * b), v - 2 * w, 9 * (b + 10), w + 10, b + (x - 10 * b), v - 2 * w)

    for m in range(len(y)):
        key = int(y[m], 16)
        new = draw_image(new, original, math.floor((key % 8 + 1) * b), math.floor((math.floor((key / 8)) + 1) * w), math.floor(b), math.floor(w), math.floor((m % 8 + 1) * (b + 10)), math.floor((math.floor(m / 8) + 1) * (w + 10)), math.floor(b), math.floor(w)); 

    return new
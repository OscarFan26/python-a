from PIL import ImageDraw, Image, ImageFont
import random

img = Image.new("RGB", (1000, 1000), "grey")
draw = ImageDraw.Draw(img)
(w, h) = img.size
for i in range(0, w, w // 50):
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	draw.line([(i, 0), (w, i)], (r, g, b))
img.save("pil_2_try1_s1.jpeg")
im = Image.open("img/pil_2_try1_s1.jpeg")
draw2 = ImageDraw.Draw(im)
draw2.text((0, 0), "Hello World!", "tomato")
img.save("pil_2_try1_s2.jpeg")

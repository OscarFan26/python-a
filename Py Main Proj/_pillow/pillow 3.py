from PIL import Image, ImageDraw, ImageFont
import random


def ascii_get():
	return chr(random.randint(30000, 40000))


def color_get():
	return random.randint(50, 100), random.randint(50, 130), 255


w = 240
h = 60
img = Image.new("RGB", (w, h), (255, 255, 255))
font = ImageFont.truetype("C:/Windows/Fonts/msyhl.ttc", 30)
draw = ImageDraw.Draw(img)

for i in range(500):
	x = random.randint(0, 240)
	y = random.randint(0, 60)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	if not i > 4:
		draw.text((60 * i + 10, 10), ascii_get(), font=font, fill=(r, g, b))
	draw.point((x, y), (r, g, b))
for j in range(20):
	x = random.randint(0, 255)
	y = random.randint(0, 255)
	xx = random.randint(0, 255)
	yy = random.randint(0, 255)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	draw.line([(x, y), (xx, yy)], (r, g, b), 1)
img.save("code_py.jpeg")

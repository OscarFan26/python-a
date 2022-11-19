from PIL import Image, ImageDraw
import random

open_it = Image.open("img/new1__image_test.png")
draw = ImageDraw.Draw(open_it)
for i in range(500000):
	x = random.randint(0, 2000)
	y = random.randint(0, 1500)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	draw_pic = draw.point((x, y), (r, g, b))

for j in range(5):
	x = random.randint(0, 2000)
	y = random.randint(0, 1500)
	x2 = random.randint(0, 2000)
	y2 = random.randint(0, 1500)
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	draw_lines = draw.line([(x, y), (x2, y2)], (r, g, b), 50)

save_pic2 = open_it.save("PIL2__Point.png")

import os
from PIL import Image

os.makedirs("withlogo", exist_ok=True)
logofileaddr = "img/py__pil_logo.png"
logof = Image.open(logofileaddr)
namelist = os.listdir("C:/Users/pc/Desktop")

for i in namelist:
	if (i.endswith(".png") or i.endswith("jpeg")) and i != "py__pil_logo.png":
		presentimg = Image.open("C:/Users/pc/Desktop/" + i)
		w, h = presentimg.size
		resized_logo = logof.resize((int(w / 10), int(h / 10)))
		presentimg.paste(resized_logo, (int(w / 10 * 9), int(h / 10 * 9)))
		presentimg.save("C:/Users/pc/Desktop/" + i)

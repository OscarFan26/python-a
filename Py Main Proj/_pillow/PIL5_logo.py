from PIL import Image, ImageDraw, ImageFont

pri_img = Image.open("C:\\Users\\pc\\Desktop\\pic2.jpeg")
new = ImageDraw.Draw(pri_img, "RGB")
w, h = pri_img.size
text = new.text((int(w - 200), int(h - 150)), "Copyright©Navicat  Oscar",
                font=ImageFont.truetype("C:/Windows/Fonts/simsun.ttc", 15))
text2 = new.text((int(w - 175), int(h - 100)), "All Rights Reserved",
                 font=ImageFont.truetype("C:/Windows/Fonts/simsun.ttc", 15),
                 fill="yellow")
pri_img.save("afterlogoed.png")

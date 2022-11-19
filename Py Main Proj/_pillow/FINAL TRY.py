from PIL import Image

"""
start time: before main
"""
pythonpic = "img/Pythonpic.png"
pythoncode = "img/pythoncode.png"
aaa = "img/aaa.png"
hi = "img/hy.png"
finalfile = Image.new("RGB", (1000, 1000), "white")
p1 = Image.open(pythonpic)
p2 = Image.open(pythoncode)
p3 = Image.open(aaa)
p4 = Image.open(hi)

"""
We will start from now


notes   0.0      .--------.--------.
                 |                 |
                 |                 |
                 |                 |
                 |-  .......       |
                 |                 |
                 |                 |
                 |                 |
                 .--------.--------.
"""
a1 = p1.resize((500, 500))
a2 = p2.resize((500, 500))
a3 = p3.resize((500, 500))
a4 = p4.resize((500, 500))
finalfile.paste(a3, (0, 0))
finalfile.paste(a4, (500, 0))
finalfile.paste(a1, (0, 500))
finalfile.paste(a2, (500, 500))

finalfile.save("img/4pic_alt.jpeg")

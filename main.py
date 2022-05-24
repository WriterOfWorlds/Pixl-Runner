from PIL import Image

def command(pixel):
    commands = {
        "(255, 0, 0, 255)": "Red",
        "(0, 255, 0, 255)": "Green",
        "(0, 0, 255, 255)": "Blue",
        "(255, 255, 0, 255)": "Yellow",
        "(255, 0, 255, 255)": "Purple",
        "(0, 255, 255, 255)": "Aqua",
        "(0, 0, 0, 255)": "Black",
        "(255, 255, 255, 255)": "White"
    }
    pixel = str(pixel)
    for x, y in commands.items():
        if pixel == x:
            try:
                call(y)
            except:
                print(y)

im = Image.open("image.png")
pix = im.load()
x = 0
y = 0
error = 0
while True:
    try:
        command(pix[x,y])
        x += 1
        error = 0
    except:
        y += 1
        x = 0
        error += 1
        if error > 5:
            break
from PIL import Image
import time
import os
import math
import sys

symbols = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
symbolList = list(symbols)
numSymbols = len(symbolList)
step = numSymbols / 256

bigger = 0.1
waitTime = 0.0

def findSymbol(number):
    return symbolList[math.floor(number * step)]

def picToAscii(pic):
    pic = pic.convert('RGB')
    w, h = pic.size
    pic = pic.resize((int(bigger * w), int(bigger * h)), Image.NEAREST)
    w, h = pic.size
    pixels = pic.load()

    asciiPic = ""
    for y in range(h):
        for x in range(w):
            red, green, blue = pixels[x, y]
            gray = int(red / 3 + green / 3 + blue / 3)
            asciiPic += findSymbol(gray)
        asciiPic += '\n'
    return asciiPic

def cleanScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

currentFolder = os.path.dirname(os.path.realpath(sys.argv[0]))
gifName = os.path.join(currentFolder, 'amogus-among-us.gif')

gifImage = Image.open(gifName)

while True:
    try:
        asciiPicture = picToAscii(gifImage)
        cleanScreen()
        print(asciiPicture)
        time.sleep(waitTime)

        gifImage.seek(gifImage.tell() + 1)
    except EOFError:
        gifImage.seek(0)

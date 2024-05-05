from PIL import Image
import os
from KNearestNeighbors import K_NearestNeighbors as knn
import shutil
import uuid
def cvtToList(img_path):
    image = Image.open(img_path)

    grayIMG = image.convert("L")

    pixels = list(grayIMG.getdata())
    
    return pixels

idata = {}

directory1 = 'images/circle'

for filename in os.listdir(directory1):
    f = os.path.join(directory1, filename)
    if os.path.isfile(f):
        idata[tuple(cvtToList(f))] = "circle"

directory2 = 'images/triangle'

for filename in os.listdir(directory2):
    f = os.path.join(directory2, filename)
    if os.path.isfile(f):
        idata[tuple(cvtToList(f))] = "triangle"

k = knn(idata)

predicted = k.predict(cvtToList("/home/whaleza/Desktop/imgclassification/test.png"), 16000)
if predicted == None:
    imgT = input("None: What is that? ")
    shutil.copyfile('./test.png', "./images/"+imgT+"/" + str(uuid.uuid4()).replace("-", "") + ".png")
else:
    crt = input(f"Is this a {predicted}? ")
    if crt == "y":
        shutil.copyfile('./test.png', "./images/"+predicted+"/" + str(uuid.uuid4()).replace("-", "") + ".png")
        print("YESSSSS")
    elif crt == "n":
        imgT = input("I'm sorry, but what is it? ")
        shutil.copyfile('./test.png', "./images/"+imgT+"/" + str(uuid.uuid4()).replace("-", "") + ".png")


import os
from PIL import Image

PATH = "input"

#Creates a list of all image names
img_names = os.listdir(PATH)

if len(img_names) < 1:
    print("No images found...")
else:
    #Opens the image and puts in a list
    images = []
    for name in  sorted(img_names):
        image = Image.open(PATH + "/" + name)
        images.append(image)

    img_params = list(images)
    img_params.pop(0)

    images[0].save("output/success.gif", save_all=True, append_images=img_params, duration=200,loop=0,)
    print("Your GIF has been generated and saved in 'Output' folder..")



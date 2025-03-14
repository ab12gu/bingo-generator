#
# filename: bingo-generator.py
# by: Abhay Gupta
# date created: 24-03-14
#
# intent: generate a bingo board in the shape of a pie with pie pieces

import os
import sys
import math
import random
from PIL import Image

def main():
    """ runs pie generator """

    directory = "./images/pies/"
    pies = []
    imgs = []

    # add images to an array
    for entry in os.scandir(directory):
        try:
            with Image.open(entry) as img:
                print(entry.path)
                pies.append(entry)
                imgs.append(img)

        except (IOError, SyntaxError):
            pass

    print(pies)

    for pie in pies:
        pass
        

        #img = Image.open(pie)
        #img.show()

    images = [Image.open(x) for x in pies]

    ## shuffle images
    random.shuffle(images)

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    total_height = sum(heights)

    offset = 2.15

    new_im = Image.new('RGB', (round(total_width/offset), round(total_height/offset), "WHITE"))

    # create a circle 
    length = 5
    distance = 8
    circles = 3

    x_coords = []
    y_coords = []
    
    offset = 1.6

    for i in range(circles):
        diameter = (i+1) * widths[0] 
    
        for j in range(distance):
            y_coords.append(offset * diameter * math.sin(2*math.pi * j/distance) )
            x_coords.append(offset * diameter * math.cos(2*math.pi * j/distance) )

    print("x_coords", x_coords)
    print("y_coords", y_coords)

    offset = abs(min(y_coords + x_coords))

    for im in images:
      new_im.paste(im, (round(offset + x_coords.pop()),round(offset + y_coords.pop())))
    
            

    #x_offset = 0
    #y_offset = 0
    #for im in images:
      #new_im.paste(im, (x_offset,y_offset))
      #x_offset += im.size[0]
      #y_offset += im.size[1]
    
    # store and show final images
    new_im.save('bingo-card.jpg')
    new_im.show()




if __name__ == "__main__":
    """ calls main program initializes test cases """

    main()




























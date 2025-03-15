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
    
    cards = 36

    for c in range(cards):

        ## shuffle images
        random.shuffle(images)

        widths, heights = zip(*(i.size for i in images))

        total_width = sum(widths)
        total_height = sum(heights)

        offset = 2.15

        background = Image.open("./images/pumpkin-pie.png")
        width = round(total_width/offset)
        height = round(total_height/offset)

        new_im = Image.new('RGB',(width, height), "WHITE")
        rnew_im = background.resize((width, height))
        new_im = rnew_im.convert('RGB')

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

        center = Image.open("./images/steve.png")
        center = center.resize((widths[0], heights[0]))

        offsety = 100
        offsetx = 100
       
        new_im.paste(center, (width//2 - widths[0]+offsetx, height//2 - heights[0]+offsety))
                

        #x_offset = 0
        #y_offset = 0
        #for im in images:
          #new_im.paste(im, (x_offset,y_offset))
          #x_offset += im.size[0]
          #y_offset += im.size[1]
        
        # store and show final images
        new_im.save('./bingo-cards/card' + str(c) + '.jpg')
        #new_im.show()




if __name__ == "__main__":
    """ calls main program initializes test cases """

    main()




























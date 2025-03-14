#
# filename: bingo-generator.py
# by: Abhay Gupta
# date created: 24-03-14
#
# intent: generate a bingo board in the shape of a pie with pie pieces

import os
from PIL import Image
import sys

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

    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save('test.jpg')




if __name__ == "__main__":
    """ calls main program initializes test cases """

    main()



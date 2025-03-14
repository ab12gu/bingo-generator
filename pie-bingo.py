#
# filename: bingo-generator.py
# by: Abhay Gupta
# date created: 24-03-14
#
# intent: generate a bingo board in the shape of a pie with pie pieces

import os
from PIL import Image

def main():
    """ runs pie generator """

    directory = "./images/pies/"
    pies = []

    # add images to an array
    for entry in os.scandir(directory):
        try:
            with Image.open(entry) as img:
                print(entry.path)
                pies.append(entry)
        except (IOError, SyntaxError):
            pass

    print(pies)

    for pie in pies:
        pass
        

        #img = Image.open(pie)
        #img.show()



if __name__ == "__main__":
    """ calls main program initializes test cases """

    main()



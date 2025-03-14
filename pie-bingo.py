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

    for entry in os.scandir(directory):
        print(entry.path)

        img = Image.open(entry)
        img.show()
    



if __name__ == "__main__":
    """ calls main program initializes test cases """

    main()



'''
This script should accept as command line arguments a file name and then 
display that file using th egraphics Plus libary
'''

#import in the graphics libary and the libary needed for CLI
import graphicsPlus as graphics
import sys
import random

import filter

#k is the index for different filter selection
k = -1

#get the size and color for the text on image
size = input("please select text size:\n")
color = input("please select color('red', 'green', 'blue'):\n")

#select different filter option according to k, return the filter name string
def filter_select(image):
    if k == 0:
        return "Orginal"
    elif k == 1:
        filter.swapRedBlue(image)
        return "SwapRedBlue"
    elif k == 2:
        filter.negative(image)
        return "Negative"
    elif k == 3:
        filter.blue(image)
        return "Blue"
    elif k == 4:
        filter.red(image)
        return "Red"
    elif k == 5:
        filter.green(image)
        return "Green"
    elif k == 6:
        filter.bright(image)
        return "Bright"
    elif k == 7:
        filter.gray(image)
        return "Gray"

#main function
def main(argv):

    #check to make sure you have the correct number of arguments
    #print a usage statement if needed
        src_image = graphics.Image(graphics.Point(0, 0), argv[1])

        '''
        create variables for width and height load them with the 
        appropriate methods
        '''

        width = src_image.getWidth();
        height = src_image.getHeight();

        '''
        create a variable to hold a window object and create that object
        with GraphWin()
        '''
        
        window = graphics.GraphWin("Image", width * int(argv[2]), height * int(argv[2]))

        '''
        move the image to the center of the window. The center would be
        1/2 the width and 1/2 the height
        '''
        src_image.move(width / 2, height/2)

        '''
        create a variable to hold the image load it in with the Image 
        method from the imported lib
        '''
        #nested for loops for creating grids, the arg[2] is the number of images in a row
        for i in range(int(argv[2])):
            for j in range(int(argv[2])):
                #if user input one image only
                if len(sys.argv) == 3:
                    image = graphics.Image(graphics.Point(width * i, height * j), argv[1])
                #if user input two image 
                #the the first image will be in odd column
                elif len(sys.argv) == 4 and i % 2 == 1:
                    image = graphics.Image(graphics.Point(width * i, height * j), argv[1])
                #second image will be in even column
                elif len(sys.argv) == 4 and i % 2 == 0:
                    image = graphics.Image(graphics.Point(width * i, height * j), argv[3])

                #updating index for filter selection
                global k
                k += 1
                k %= 8

                #get the filter name string
                s = filter_select(image)

                #create a text with string s
                text = graphics.Text(graphics.Point(width * i, height * j), s)
                
                #add size and color to text, if user input is wrong, use default size and color
                global size
                global color
                try:
                    text.setSize(int(size))
                    text.setTextColor(color)
                except BaseException:
                    pass

                #draw images on the window, adjust position
                image.draw(window)
                image.move(width / 2, height/2)

                #draw texts on the window, adjust position
                text.draw(window)
                text.move(width/2, height/2)
        '''
        draw the image and then call the getMouse method to pause
        '''
        window.getMouse()
        
                 
#conditional call to pass sys.argv list to the main function
if __name__ == "__main__":
	main(sys.argv)

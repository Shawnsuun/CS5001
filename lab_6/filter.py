'''
Contains filter functions used to manipulate image files
'''

import graphicsPlus as graphics
import sys

#get RGB value for each pixel and swap R and B value of that pixel in src_image
def swapRedBlue(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by swapping the r and b values
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            src_image.setPixel(x, y, graphics.color_rgb(b, r, g))

#get RGB value for each pixel and swap RGB values to an average gray value
def gray(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by swapping the rgb values to a same average gray value
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            src_image.setPixel(x, y, graphics.color_rgb(int(0.3 * r + 0.59 * g + 0.11 * b), int(0.3 * r + 0.59 * g + 0.11 * b), int(0.3 * r + 0.59 * g + 0.11 * b)))

#get RGB value for each pixel and update r/g/b value of that pixel with 255 - r/g/b respectively
def negative(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by using 255 - r/g/b, instead of original r/g/b value
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            src_image.setPixel(x, y, graphics.color_rgb(255 - r, 255 - g, 255 - b))

#get RGB value for each pixel and increase r/g/b value with a parameter 1.2 respectively, RGB value not exceed 255
def bright(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by using r/g/b  * 1.2, instead of original r/g/b value, RGB value not exceed 255
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            r = int(min(pixel[0] * 1.2, 255))
            g = int(min(pixel[1] * 1.2, 255))
            b = int(min(pixel[2] * 1.2, 255))
            src_image.setPixel(x, y, graphics.color_rgb(r, g, b))

#get RGB value for each pixel and update r, g value to 0, b remain the same to get a blue filter
def blue(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by updating r, g value to 0, b remain the same to get a blue filter
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            b = pixel[2]
            src_image.setPixel(x, y, graphics.color_rgb(0, 0, b))

#get RGB value for each pixel and update g, b value to 0, r remain the same to get a red filter
def red(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by updating g, b value to 0, r remain the same to get a red filter
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            r = pixel[0]
            src_image.setPixel(x, y, graphics.color_rgb(r, 0, 0))

#get RGB value for each pixel and update r, b value to 0, g remain the same to get a green filter
def green(src_image):
    '''
    iterate over every pixel in the image and save the r,g, and b values in variables
    change the existing pixel by updating r, b value to 0, g remain the same to get a green filter
    '''
    width = src_image.getWidth()
    height = src_image.getHeight()

    #set up a nested for loop to traverse entire image
    for y in range(height):
        for x in range(width):
            pixel = src_image.getPixel(x, y)
            g = pixel[1]
            src_image.setPixel(x, y, graphics.color_rgb(0, g, 0))
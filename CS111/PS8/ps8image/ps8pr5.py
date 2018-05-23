#
# ps8pr5.py  (Problem Set 8, Problem 5)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import *

def create_uniform_image(height, width, pixel):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels have the RGB values
        given by pixel
        inputs: height and width are non-negative integers
                pixel is a 1-D list of RBG values of the form [R,G,B],
                     where each element is an integer between 0 and 255.
    """
    pixels = []

    for r in range(height):
        row = [pixel] * width
        pixels += [row]

    return pixels

def blank_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are green.
        inputs: height and width are non-negative integers
    """
    all_green = create_uniform_image(height, width, [0, 255, 0])
    return all_green

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

## put your functions below

def bw(pixels, threshold):
    """ returns a new 2-D list of pixels for an image that is a
    black-and-white version of the original image """
    new_pixels = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            if brightness(pixels[r][c]) > threshold:
                new_pixels[r][c] = [255, 255, 255]
            else:
                new_pixels[r][c] = [0, 0, 0]
    return new_pixels

def flip_horiz(pixels):
    """ returns a new 2-D list of pixels for an image in which the original
    image is “flipped” horizontally """
    new_pixels = blank_image(len(pixels), len(pixels[0]))
    for r in range(len(pixels)):
        for c in range(len(pixels[0])):
            new_pixels[r][c] = pixels[r][len(pixels[0]) - 1 - c]
    return new_pixels

def extract(pixels, rmin, rmax, cmin, cmax):
    """ returns a new 2-D list that represents the portion of the original
    image that is specified by the other four parameters """
    new_pixels = blank_image(rmax - rmin, cmax - cmin)
    for r in range(rmin, rmax):
        for c in range(cmin, cmax):
            new_pixels[r - rmin][c - cmin] = pixels[r][c]
    return new_pixels

def transpose(pixels):
    """ creates and returns a new 2-D list that is the transpose of pixels
    """
    new_pixels = blank_image(len(pixels[0]), len(pixels))
    for c in range(len(pixels[0])):
        tmp_new_pixels = []
        for r in range(len(pixels)):
            tmp_new_pixels += [pixels[r][c]]
        new_pixels[c] = tmp_new_pixels
    return new_pixels

def rotate_clockwise(pixels):
     """ rotate the original image clockwise by 90 degrees """
     new_pixels = blank_image(len(pixels[0]), len(pixels))
     for c in range(len(pixels[0])):
         tmp_new_pixels = []
         for r in range(len(pixels)):
             tmp_new_pixels += [pixels[len(pixels) -1 - r][c]]
         new_pixels[c] = tmp_new_pixels
     return new_pixels
            
def rotate_counterclockwise(pixels):
    """ rotate the original image counterclockwise by 90 degrees """
    new_pixels = blank_image(len(pixels[0]), len(pixels))
    for c in range(len(pixels[0])):
         tmp_new_pixels = []
         for r in range(len(pixels)):
             tmp_new_pixels += [pixels[r][len(pixels[0]) -1 - c]]
         new_pixels[c] = tmp_new_pixels
    return new_pixels

"""
1. Using numpy arrays, create a 800x800 black and white image having a pattern of alternating white and black horizontal stripes. The width of the stripe is 100
"""

#Import required libraries
import cv2
import numpy as np

#Width and height of the image
width = 800
height = 800
#Width of the stripe
stripeWidth = 100

#Create a black image
#np.zeros -> that's why it's entirely black
img = np.zeros((width, height, 3), dtype = np.uint8)

y = 0
while y*stripeWidth*2+stripeWidth < height:
    #Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
    #cv2.rectangle -> method used to draw a rectangle on an image
    #image -> on which rectangle is to be drawn
    #start_point -> starting coordinates of rectangle (X coordinate value, Y coordinate value)
    #end_point -> ending coordinates of rectangle (X coordinate value, Y coordinate value)
    #color -> Color of the rectangle to be drawn (white)
    #thickness -> Thickness of -1 px will fill the rectangle shape by the specified color
    cv2.rectangle(img, (0, y*stripeWidth*2), (width, y*stripeWidth*2+stripeWidth), (255, 255, 255), -1) 
    y += 1

#Display the image using OpenCV
cv2.imshow('Alternating White and Black Horizontal Stripes', img)
cv2.waitKey(0)

"""
2. Same as 1 but this time create vertical stripes
"""

#Import required libraries
import cv2
import numpy as np

#Width and height of the image
width = 800
height = 800
#Width of the stripe
stripeWidth = 100

#Create a black image
img = np.zeros((width, height, 3), dtype = np.uint8)

y = 0
while y*stripeWidth*2+stripeWidth < width:
    #Syntax: cv2.rectangle(image, start_point, end_point, color, thickness)
    #cv2.rectangle -> method used to draw a rectangle on an image
    #image -> on which rectangle is to be drawn
    #start_point -> starting coordinates of rectangle (X coordinate value, Y coordinate value)
    #end_point -> ending coordinates of rectangle (X coordinate value, Y coordinate value)
    #color -> Color of the rectangle to be drawn (white)
    #thickness -> Thickness of -1 px will fill the rectangle shape by the specified color
    #Exactly the same with #1 except that the X coordinate and value and Y coordinate values interchanged
    cv2.rectangle(img, (y*stripeWidth*2, 0), (y*stripeWidth*2+stripeWidth, width), (255, 255, 255), -1) 
    y += 1

#Display the image using OpenCV
cv2.imshow('Alternating White and Black Vertical Stripes', img)
cv2.waitKey(0)

"""
3. Challenge: Same as 1 but create a chessboard pattern
"""

#Import required libraries
import cv2
import numpy as np

#Width and height of the image
width = 800
height = 800
#Width of the stripe
stripeWidth = 100
#BGR color code of white
white = (255, 255, 255)

#Create a black image
img = np.zeros((width, height, 3), dtype = np.uint8)

y = 0
offset = False
while y * stripeWidth + stripeWidth <= height:
    #Returns back to 0 after every row
    x = 0
    while x * (stripeWidth * 2) + stripeWidth <= width:
        #For the odd number of rows
        topLeft = (x * stripeWidth * 2, y * stripeWidth)
        bottomRight = (x * stripeWidth * 2 + stripeWidth, y * stripeWidth + stripeWidth)
        #For the even number of rows
        if offset:
            topLeft = (x * stripeWidth * 2 + stripeWidth, y * stripeWidth)
            bottomRight = (x * stripeWidth * 2 + stripeWidth + stripeWidth, y * stripeWidth + stripeWidth)

        cv2.rectangle(img, topLeft, bottomRight, white, -1)
        #Increments after every square 
        x += 1
    #After every row, the offset changes and the y value increments (y for first row is 0, y for second row is 1, and so on)
    offset = not offset
    y += 1

#Display the image using OpenCV
cv2.imshow('Chessboard Pattern (B&W)', img)
cv2.waitKey(0)

"""
4. Challenge+: Do 1 to 3 but stripes are in different colors, choose your own colors.
"""

import cv2
import numpy as np

width = 800
height = 800
stripeWidth = 100

img = np.zeros((width, height, 3), np.uint8)
#BGR color code of red
img[:] = (0, 0, 255)

y = 0
while y*stripeWidth*2+stripeWidth < height:
    #Changed the color to green (BGR color code of green)
    cv2.rectangle(img, (0, y*stripeWidth*2), (width, y*stripeWidth*2+stripeWidth), (0, 255, 0), -1) 
    y += 1

cv2.imshow('Alternating Red and Green Horizontal Stripes', img)
cv2.waitKey(0)


import cv2
import numpy as np

width = 800
height = 800
stripeWidth = 100

img = np.zeros((width, height, 3), dtype = np.uint8)
#BGR color code of Regent St Blue
img[:] = (231, 199, 167)

y = 0
while y*stripeWidth*2+stripeWidth < width:
    #Changed the color to pastel pink (BGR color code of pastel pink)
    cv2.rectangle(img, (y*stripeWidth*2, 0), (y*stripeWidth*2+stripeWidth, width), (220, 200, 248) , -1) 
    y += 1

cv2.imshow('Alternating Regent St Blue and Pastel Pink Vertical Stripes', img)
cv2.waitKey(0)


import cv2
import numpy as np

width = 800
height = 800
stripeWidth = 100
#BGR color code of cream
cream = (153, 198, 225)

img = np.zeros((width, height, 3), dtype = np.uint8)
#BGR color code of dark brown
img[:] = (51, 64, 92)

y = 0
offset = False
while y * stripeWidth + stripeWidth <= height:
    x = 0
    while x * (stripeWidth * 2) + stripeWidth <= width:
        topLeft = (x * stripeWidth * 2, y * stripeWidth)
        bottomRight = (x * stripeWidth * 2 + stripeWidth, y * stripeWidth + stripeWidth)

        if offset:
            topLeft = (x * stripeWidth * 2 + stripeWidth, y * stripeWidth)
            bottomRight = (x * stripeWidth * 2 + stripeWidth + stripeWidth, y * stripeWidth + stripeWidth)

        cv2.rectangle(img, topLeft, bottomRight, cream, -1)
        x += 1
    offset = not offset
    y += 1

cv2.imshow('Chessboard Pattern (Dark Brown & Cream)', img)
cv2.waitKey(0)
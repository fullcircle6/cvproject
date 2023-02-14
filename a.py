# Create a blank canvas using NumPy and display any color palette of your choice using OpenCV
# Import required modules
import cv2
import numpy as np


# Create a white canvas
def createCanvas(color):
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    canvas[:] = color
    return canvas


# Display two images using OpenCV in two different windows press key 'q' to close the window
# set the window title with Canvas and Palette
def displayImage(images):
    cv2.imshow("Canvas", images[0])
    cv2.imshow("Palette", images[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    # Create canvas
    # Use the createCanvas function
    # you have written above
    canvas = createCanvas((255, 255, 255))
    # Load the color palette,set the image width and height to 300
    palette = cv2.imread("img/palette.jpeg", cv2.IMREAD_UNCHANGED)
    palette = cv2.resize(palette, (300, 300))
    # Display the canvas and  Use the functions you have written above
    displayImage([canvas, palette])
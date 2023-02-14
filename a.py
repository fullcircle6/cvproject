# Create a blank canvas using NumPy and display any color palette of your choice using OpenCV
# Import required modules
import cv2
import numpy as np


# Create a white canvas
def createCanvas(color):
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    canvas[:] = color
    return canvas


# Display an image using OpenCV press any key to close the image, set the image width and height
def displayImage(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Load the color palette
def loadPalette():
    palette = cv2.imread("img/palette.jpeg")
    return palette


if __name__ == '__main__':
    # Create canvas
    # Use the createCanvas function
    # you have written above
    canvas = createCanvas((255, 255, 255))
    # Display the canvas and  Use the functions you have written above
    displayImage(canvas)
    # Display the color palette and  Use the functions you have written above
    palette = loadPalette()
    displayImage(palette)

# Create a blank canvas using NumPy and display any color palette of your choice using OpenCV
# Import required modules
import cv2
import numpy as np


# Create a white canvas
def createCanvas(color):
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    canvas[:] = color
    return canvas


# Display two images using OpenCV in two different windows
# set the window title with Canvas and Palette
# use the mouse callback function to pick the color from the palette,
# blend it with the color present in the canvas,
# and overwrite the canvas color with the newly obtained color.
def displayImage(images):
    cv2.namedWindow("Canvas", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Palette", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("Palette", mouseCallbackFunction)
    cv2.imshow("Canvas", images[0])
    cv2.imshow("Palette", images[1])
    # if Esc key was pressed ,then check if the user pressed r (for reset) or s (for save) key.
    # If the user pressed r, then reset the canvas to white.
    # If the user pressed s, then save the canvas to a file.
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            key = cv2.waitKey(0) & 0xFF
            if key == ord("r"):
                cv2.imshow("Canvas", createCanvas((255, 255, 255)))
            elif key == ord("s"):
                cv2.imwrite("img/canvas.jpg", canvas)
            else:
                cv2.waitKey(0)
                cv2.destroyAllWindows()


# Create a mouse callback function that tracks the location of the cursor on the color palette display window
def mouseCallbackFunction(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse is at ({}, {})".format(x, y))
        color = findColor(palette, x, y)
        print("Color is {}".format(color))
        color = mixColors(color, findColor(canvas, x, y))
        print("New color is {}".format(color))
        cv2.imshow("Canvas", createCanvas(color))
        print("Canvas updated", canvas)
# Find the color for an image at the given location
def findColor(img,x,y):
    return img[y,x]
# Mix two colors
def mixColors(color1, color2):
    return tuple(map(lambda x, y: (x + y) // 2, color1, color2))

# click the mouse on the palette to change the color of the canvas and display the new canvas

if __name__ == '__main__':
    # Create canvas
    # Use the createCanvas function
    # you have written above
    canvas = createCanvas((255, 255, 255))
    # Load the color palette,set the image width and height to 300
    palette = cv2.imread("img/palette.jpeg")
    palette = cv2.resize(palette, (300, 300))
    # Display the canvas and  Use the functions you have written above
    displayImage([canvas, palette])


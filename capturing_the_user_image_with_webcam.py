# Load the image of the face mask
# Load the image of the face mask using OpenCV and display it using OpenCV.
# import libraries
import cv2
import numpy as np


def show_mask():
    # load the image of the face mask The image has a transparent background
    image = cv2.imread("img/mask.png", cv2.IMREAD_UNCHANGED)
    # Extract the alpha channel from the image
    alpha = image[:, :, 3]
    # Display the alpha channel and the face mask using OpenCV
    images = [image, alpha]
    # when show the alpha and face Mask, let the window side by side
    cv2.namedWindow("Alpha", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Face Mask", cv2.WINDOW_NORMAL)
    cv2.imshow("Alpha", images[0])
    cv2.imshow("Face Mask", images[1])
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Create a cv2.VideoCapture object and capture the image from the webcam
def captureImage():
    # Create a cv2.VideoCapture object
    # Capture the image from the webcam
    # Return the captured image
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow("Image", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite("img/capture.png", frame)
            return frame
if __name__ == '__main__':
    show_mask()
    # Capture the image from the webcam
    frame = captureImage()
    if frame is not None:
        cv2.imshow("Image", frame)
        cv2.waitKey(0)
        cv2.destroyAllWindows()










#%%

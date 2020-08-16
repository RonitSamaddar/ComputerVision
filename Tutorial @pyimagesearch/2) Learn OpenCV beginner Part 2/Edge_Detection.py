# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-m", "--minT", required=True,
	help="minimum threshold for edge detection")
ap.add_argument("-M", "--maxT", required=True,
	help="minimum threshold for edge detection")
args = ap.parse_args()

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(args.image)
cv2.imshow("Image", image)
# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

edged = cv2.Canny(gray, int(args.minT), int(args.maxT))#Higher the threshold, lesser the edges detected (based on how much
#difference there is in both sides of the edge
cv2.imshow("Edged", edged)
cv2.waitKey(0) 
#Using the popular Canny algorithm
# import the necessary packages
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-m", "--minT", required=True,
	help="minimum threshold")
ap.add_argument("-M", "--maxT", required=True,
	help="minimum threshold")
args = ap.parse_args()

# load the input image (whose path was supplied via command line
# argument) and display the image to our screen
image = cv2.imread(args.image)
cv2.imshow("Image", image)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray", gray)

# threshold the image by setting all pixel values less than "minT"
# to (white; foreground) and all pixel values >= "minT" and <= "maxT"
# to (black; background), thereby segmenting the image
thresh = cv2.threshold(gray, int(args.minT), int(args.maxT), cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
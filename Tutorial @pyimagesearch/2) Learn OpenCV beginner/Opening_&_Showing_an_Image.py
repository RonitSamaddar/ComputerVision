import argparse
import imutils
import cv2

#Defining command line arguments
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path for input file')
args=ap.parse_args()


#Reading the image
img=cv2.imread(args.image)
(h,w,d)=img.shape
print("Height = {}, Width = {}, Depth = {}".format(h,w,d))

#Showing the image
cv2.imshow("IMAGE",img)
cv2.waitKey(0)
cv2.destroyAllWindows();


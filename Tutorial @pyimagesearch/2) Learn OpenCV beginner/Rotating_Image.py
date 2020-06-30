import argparse
import imutils
import cv2

#Defining command line arguments
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path for input file')
ap.add_argument('-d','--degree',required=True,help='degree to be rotated')
args=ap.parse_args()


#Reading the image
img=cv2.imread(args.image)
(h,w,d)=img.shape
print("Height = {}, Width = {}, Depth = {}".format(h,w,d))

#Showing the image
cv2.imshow("IMAGE",img)


center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, float(args.degree), 1.0) # we will rotate by -90 degree anticlockwise, i.e. 45 degree clockwise
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow(args.degree +" degree anti-clockwise Rotated Image", rotated)


cv2.waitKey(0)
cv2.destroyAllWindows();
import argparse
import imutils
import cv2

#Defining command line arguments
ap=argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='path for input file')
ap.add_argument('-b','--blur',required=True,help='blur kernel size')
args=ap.parse_args()




#Reading the image
img=cv2.imread(args.image)
(h,w,d)=img.shape
print("Height = {}, Width = {}, Depth = {}".format(h,w,d))

#Showing the image
cv2.imshow("IMAGE",img)


f=int(args.blur)
if(f%2==0):
	f=f+1
#f=int(args.blur)*1.0/100*dim
# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
# Larger the kernel higher the blur
blurred = cv2.GaussianBlur(img, (f, f), 0)
cv2.imshow("BLURRED IMAGE", blurred)


cv2.waitKey(0)
cv2.destroyAllWindows();
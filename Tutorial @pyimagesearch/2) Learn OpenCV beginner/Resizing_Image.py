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


#Resizing the image
#cv2.resize(img,(width,height))

# 1) without considering aspect ratio

img2=cv2.resize(img,(200,200))
cv2.imshow("RESIZED IMAGE 1",img2)

# 2) considering aspect ratio
img3=imutils.resize(img,width=200)
cv2.imshow("RESIZED IMAGE 2",img3)


cv2.waitKey(0)
cv2.destroyAllWindows();


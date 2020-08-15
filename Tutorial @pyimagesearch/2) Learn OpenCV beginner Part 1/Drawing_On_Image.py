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

# draw a 2px thick red rectangle and a blue circle
x1=w//4
y1=h//4
x2=3*x1
y2=3*y1
xc=w//2
yc=h//2
output = img.copy()#We copy the image as cv2.rectangle directly draws on the image given in the parameter

cv2.rectangle(output, (x1-50, y1-50), (x1+50, y1+50), (0, 0, 255), 5)
#cv2.rectangle(img,(start_point),(end_point),(colour),thickness)

cv2.circle(output, (x2, y2), 50, (255, 0, 0), 5)#Put last parameters -1 for filled up
#cv2.circle(img,(centre_point),radius,(colour),thickness)

cv2.rectangle(output, (x2-50, y1-50), (x2+50, y1+50), (0, 0, 255), -1)
cv2.circle(output, (x1, y2), 50, (255, 0, 0), -1)

cv2.line(output, (x1, y1), (x2, y2), (0, 255, 0), 5)
#cv2.line(img,(start_point),(end_point),(colour),thickness)

cv2.putText(output, "OpenCV + Jurassic Park!!!", (x1, yc-5), 
	cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#cv2.putText(img,text,(start_point),font,scale,(colour),thickness)

cv2.imshow("IMAGE DRAWN OVER", output)
cv2.waitKey(0)



cv2.waitKey(0)
cv2.destroyAllWindows();
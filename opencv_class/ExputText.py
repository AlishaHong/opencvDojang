import numpy as np
import cv2,sys

Textimg = np.full((400,400,3),255, np.uint8)
Lineimg = np.full((400,400,3),255, np.uint8)
Recimg = np.full((400,400,3),255, np.uint8)
Cirimg = np.full((400,400,3),255, np.uint8)

text = 'hihihi'
font = cv2.FONT_HERSHEY_COMPLEX
fontsize = 1
fontColor = (255,0,0)
thick = 3
linetype = cv2.LINE_AA
cv2.putText(Textimg,text,(50,350),font,fontsize,fontColor,thick,linetype)
cv2.imshow('img', Textimg)
key = cv2.waitKey(0)


pt1 = (50,100)
pt2 = (Lineimg.shape[0]-50, 100)
pt3 = (Lineimg.shape[0]-50, 200)
pt4 = (Lineimg.shape[0]-50, 300)
pt6 = (Lineimg.shape[0]-50, 400)
pt5 = (200,300)
linecolor = (0,0,255)
linecolor2 = (0,255,0)
thickness = 3
linetype = cv2.LINE_8

cv2.line(Lineimg, pt1,pt2,linecolor,thickness,linetype)
cv2.line(Lineimg, pt1,pt3,linecolor2,thickness,cv2.LINE_4)
cv2.line(Lineimg, pt1,pt4,linecolor2,thickness,cv2.LINE_AA)
cv2.line(Lineimg, pt1,pt6,linecolor,thickness,cv2.LINE_AA)

cv2.imshow('img', Lineimg)

# (x1,y1), (x2,y2)
cv2.rectangle(Recimg,pt1,pt5,linecolor,thickness,linetype)
# x,y,w,h 
cv2.rectangle(Recimg,(50,100,100,100),linecolor2 ,thickness,linetype)
cv2.imshow('rec',Recimg)


cv2.circle(Cirimg, (int(Cirimg.shape[0]/2), int(Cirimg.shape[1]/2)), 100, (120,255,0),2,cv2.LINE_AA)
cv2.imshow('circle',Cirimg)

key = cv2.waitKey(0)
if key == ord('q'):
    sys.exit()

cv2.destroyAllWindows()
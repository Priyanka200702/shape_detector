import cv2

photo=input("Enter the pic name you want to work on:   ")
#if ".png" not in photo:
 #  photo=photo+".png"

img=cv2.imread(photo)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,thresh=cv2.threshold(gray,150,255,cv2.THRESH_BINARY)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(img,contours,-1,(255,0,0),3)

for contour in contours:
    approx=cv2.approxPolyDP(contour,0.001*cv2.arcLength(contour,True),True)
    corners=len(approx)
   

    if corners==3:
        shape_name="triangle"
    elif corners==4:
        shape_name="Rectangle"
    elif corners==5:
        shape_name="Pentagon"
    elif corners==6:
        shape_name="polygon"
    elif corners>6:
        shape_name="circle"
    else:
        shape_name="unknown"
    
    cv2.drawContours(img,[approx],0,(125,0,125),3)
    x=approx.ravel()[0]
    y=approx.ravel()[1]
    

cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1.5,(125,125,0),1)
cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

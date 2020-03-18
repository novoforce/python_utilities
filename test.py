import cv2
img = cv2.imread('C:/Users/as20052058/Desktop/goturn_data/data_fixed/frames_dir/400/frame_1.png')
#1257,458,1267,468
curX = 53
curY = 142
cv2.rectangle(img,(curX,curY-66),(curX+20,curY+20-66),(255,0,0),2)

cv2.imshow('test',img)
cv2.waitKey(0)
import cv2
camera = cv2.VideoCapture(0)
ret,frame=camera.read()
for i in range(30):
    temp=camera.read()
ret,frame=camera.read()
cv2.imwrite('image.jpg',frame)
camera.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
input=cv2.imread(r"C:\Users\seenu\Pictures\images.jpg")
cv2.imshow('flower',input)
cv2.waitKey()
cv2.destroyAllWindows()
print(input.shape)
print('height of image',int(input.shape[0]),'pixels')
print('width of image',int(input.shape[1]),'pixels')
cv2.imwrite('output.png',input)
cv2.imwrite('output.jpg',input)








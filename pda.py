

import cv2
img=cv2.imread("C:\\Users\\Poorna Prajna D\Desktop\\abc.jpg")
img=cv2.resize(img,(1200,600))
print(img)
cv2.imshow("original",img)
cv2.waitKey()
cv2.destroyAllWindows()
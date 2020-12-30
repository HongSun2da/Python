import cv2

img_basic = cv2.imread("movie2019_5.jpg", cv2.IMREAD_COLOR)
cv2.imshow("Image Basic", img_basic)
cv2.waitKey(0)
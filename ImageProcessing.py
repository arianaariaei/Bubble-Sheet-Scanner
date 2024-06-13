import cv2


WIDTH = 600
HEIGHT = 800

image1 = cv2.imread('images/1.jpg',cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images/2.jpg',cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('images/3.jpg',cv2.IMREAD_GRAYSCALE)
image4 = cv2.imread('images/4.jpg',cv2.IMREAD_GRAYSCALE)
image5 = cv2.imread('images/5.jpg',cv2.IMREAD_GRAYSCALE)
image6 = cv2.imread('images/6.png',cv2.IMREAD_GRAYSCALE)
image7 = cv2.imread('images/7.jpg',cv2.IMREAD_GRAYSCALE)
image8 = cv2.imread('images/8.jpg',cv2.IMREAD_GRAYSCALE)

cv2.imshow('Grayscale Image', cv2.resize(image1, (WIDTH, HEIGHT)))
cv2.waitKey(0)
cv2.destroyAllWindows()
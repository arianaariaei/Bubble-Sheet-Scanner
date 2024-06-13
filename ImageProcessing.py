import cv2
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

WIDTH = 600
HEIGHT = 800

# Load images
image1 = cv2.imread('images/1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('images/2.jpg', cv2.IMREAD_GRAYSCALE)
image3 = cv2.imread('images/3.jpg', cv2.IMREAD_GRAYSCALE)
image4 = cv2.imread('images/4.jpg', cv2.IMREAD_GRAYSCALE)
image5 = cv2.imread('images/5.jpg', cv2.IMREAD_GRAYSCALE)
image6 = cv2.imread('images/6.png', cv2.IMREAD_GRAYSCALE)
image7 = cv2.imread('images/7.jpg', cv2.IMREAD_GRAYSCALE)
image8 = cv2.imread('images/8.jpg', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded correctly
if image1 is None:
    raise IOError("Error: Image 1 could not be loaded.")
# You can add similar checks for other images if needed

# Apply threshold
ret, binary1 = cv2.threshold(image1, 150, 255, cv2.THRESH_BINARY_INV)

# Find contours
contours, _ = cv2.findContours(binary1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
bubbles = [c for c in contours if 100 < cv2.contourArea(c) < 1000]

filled_bubbles = []
for bubble in bubbles:
    mask = np.zeros_like(binary1)
    cv2.drawContours(mask, [bubble], -1, 255, -1)
    mean_val = cv2.mean(binary1, mask=mask)[0]
    if mean_val > 127:
        filled_bubbles.append(bubble)

# Define region for OCR
student_id_region = image1[220:280, 850:2000]

# Perform OCR
student_id_text = pytesseract.image_to_string(student_id_region)
print(f'Student ID: {student_id_text}')
#
# # Display the image with contours
# output_image = cv2.cvtColor(binary1, cv2.COLOR_GRAY2BGR)
# cv2.drawContours(output_image, filled_bubbles, -1, (0, 255, 0), 2)
cv2.imshow('Bubbles', image1[220:280,850:2000])
cv2.waitKey(0)
cv2.destroyAllWindows()

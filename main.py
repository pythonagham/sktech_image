import cv2
from sketchpy import canvas

# Load the image
image_path = 'image.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply edge detection
edges = cv2.Canny(image, 100, 200)

# Save the processed image
processed_image_path = 'processed_image.png'
cv2.imwrite(processed_image_path, edges)

# Use sketchpy to draw the processed image
obj = canvas.sketch_from_image(processed_image_path)
obj.draw()

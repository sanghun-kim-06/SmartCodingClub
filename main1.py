import cv2

img = cv2.imread(r'OpenCV/image.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# blur = cv2.GaussianBlur(img, (5, 5), 7)
edges = cv2.Canny(img, 100, 200)

# cv2.imwrite(r'OpenCV/output.jpg', img)
# cv2.imwrite(r'OpenCV/outputGray.jpg', gray)
# cv2.imwrite(r'OpenCV/outputBlur.jpg', blur)
cv2.imwrite(r'OpenCV/outputEdges.jpg', edges)


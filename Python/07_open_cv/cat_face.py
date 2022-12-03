import cv2 as cv

print("OpenCV version:", cv.__version__)

cascade = cv.CascadeClassifier('Python/07_open_cv/cat_face_extended.xml')
img = cv.imread("images/01_cat.webp")
# img = cv.imread("images/02_cat.jpg")
print(img.shape)
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cats = cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=2)
print(len(cats), "cats found")
for cat in cats:
    print(cat)
print(cascade)

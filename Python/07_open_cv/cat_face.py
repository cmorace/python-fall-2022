import cv2 as cv
print("OpenCV version:", cv.__version__)
cascade = cv.CascadeClassifier('Python/07_open_cv/cat_face_extended.xml')
img = cv.imread("images/01_cat.webp")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cats = cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=6)
print(len(cats), "cat faces detected")
for (x, y, w, h) in cats:
    cv.rectangle(img, pt1=(x, y), pt2=(x+w, y+h),
                 color=(255, 255, 0), thickness=2)

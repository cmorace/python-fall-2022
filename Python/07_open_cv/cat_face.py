import cv2 as cv
print("OpenCV version:", cv.__version__)
cascade = cv.CascadeClassifier('Python/07_open_cv/cat_face_extended.xml')
img = cv.imread("images/01_cat.webp")
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cats = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=4)
print(f"{len(cats)} cat face{''if len(cats) == 1 else 's'} detected")
for (x, y, w, h) in cats:
    cv.rectangle(img, pt1=(x, y), pt2=(x+w, y+h),
                 color=(255, 255, 0), thickness=2)

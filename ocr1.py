import cv2
import pytesseract
img = cv2.imread("./photos/images.png")
img = cv2.resize(img,(600,600))
cv2.imshow("Image",img)
cv2.waitKey(0)
pytesseract.pytesseract.tesseract_cmd =r'E:\TESSERACT-OCR\tesseract.exe'
text = pytesseract.image_to_string(img)
print(text)
h_img,w_img, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img, (x, h_img-y),(w,h_img-h), (0,0,255), 3)
    cv2.putText(img,b[0],(x,h_img-y+25), cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)

cv2.imshow('Images',img)
cv2.waitKey(0)
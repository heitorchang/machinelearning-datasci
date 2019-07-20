import pytesseract
from pytesseract import Output
import cv2
import pyscreenshot as ImageGrab

# 

if __name__ == "__main__": 
    # imggrab = ImageGrab.grab()

    # imggrab.save('tmp.png')


    img = cv2.imread('ytmadonna.png')
    img = cv2.resize(img, None, fx=4.0, fy=4.0, interpolation=cv2.INTER_LINEAR)

    
    d = pytesseract.image_to_data(img, output_type=Output.DICT, config="--psm 12")
    for k in d:
        pass
        print(k, d[k])
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        if True:
            print(x, y, d['text'][i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

   # cv2.imshow('img', img)
   # cv2.waitKey(0)

